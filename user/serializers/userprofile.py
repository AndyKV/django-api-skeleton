from rest_framework import serializers
from user.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
	"""
	Serializing User
	"""
	class Meta:
		model = UserProfile
		fields = (
			'email',
			'password',
			'last_name',
			'first_name',
		)

		extra_kwargs = {
		    'password': {
		        'write_only': True,
		    },
		}

	def save(self, **kwargs):
		user = super().save(**kwargs)
		user.set_password(user.password)
		user.token = user.make_confirm_token()
		user.save()
		user.send_registration_email.delay(user.email, user.token)
		return user


class ActivateUserSerializer(serializers.ModelSerializer):


	class Meta:
		model = UserProfile
		fields=('is_active',)
