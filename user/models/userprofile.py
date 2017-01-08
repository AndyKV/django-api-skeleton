from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager as DefaultUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.template.loader import render_to_string

from celery_app import app as celery_app

from core.models import UUIDPKCoreModel, CoreManager
from core.lib import send_mail


class UserManager(DefaultUserManager, CoreManager):


    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, username=None, password=None, **extra_fields):
        return self._create_user(username, password,
                                 is_staff=False, is_superuser=False,
                                 **extra_fields)


    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password,
                                 is_staff=True, 
                                 is_superuser=True,
                                 is_active=True,
                                 **extra_fields)


class UserProfile(UUIDPKCoreModel, AbstractBaseUser, PermissionsMixin):
	
	email = models.EmailField(_('email address'), unique=True)
	first_name = models.CharField(_('first name'), max_length=50)
	last_name = models.CharField(_('last name'), max_length=50)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	token = models.CharField(max_length=36, blank=True, 
							default=uuid4, unique=True)

	USERNAME_FIELD = 'email'
	objects = UserManager()


	class Meta:
	    swappable = 'AUTH_USER_MODEL'


	def make_confirm_token(self):
		return uuid4()


	def get_full_name(self):
		return '{} {}'.format(self.first_name, self.last_name)


	def get_short_name(self):
		return self.first_name


	def __str__(self):
		return self.email


	@celery_app.task
	def send_registration_email(email, token):
		link = 'https://{site}/activate-user/{token}'.format(**{
				'site': settings.BASE_URL,
				'token': token,
		})
		
		message = render_to_string('emails/register_success.html', {'confirmation_link': link})
		
		msg_data = {
			'recipient_list': [email],
			'html_message': message,
			'from_email': settings.DEFAULT_EMAIL,  
			'subject': settings.EMAIL_REGISTRATION_TITLE,
			'message': message,
		}
		
		send_mail(**msg_data)
		return 'Message sent.'


	@celery_app.task
	def send_reset_password_mail(email, token):
		link = 'https://{site}/reset-password/{token}'.format(**{
				'site': settings.BASE_URL,
				'token': token,
		})
		
		message = render_to_string('emails/password_reset.html', {'confirmation_link': link})
		
		msg_data = {
			'recipient_list': [email],
			'html_message': message,
			'from_email': settings.DEFAULT_EMAIL,  
			'subject': settings.EMAIL_PASSWORD_RESET_TITLE,
			'message': message,
		}
		
		send_mail(**msg_data)
		return 'Message sent.'
