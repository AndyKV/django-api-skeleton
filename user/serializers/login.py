import datetime

from django.utils import timezone
from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _

from rest_framework import serializers
from rest_framework_jwt.compat import Serializer, get_username_field, PasswordField
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler


#Update base jwt token login class to add remember me functionality
class JSONWebTokenSerializer(Serializer):
	"""
	Serializer class used to validate a username and password.
	'username' is identified by the custom UserModel.USERNAME_FIELD.
	Returns a JSON Web Token that can be used to authenticate later calls.
	"""
	def __init__(self, *args, **kwargs):
		"""
		Dynamically add the USERNAME_FIELD to self.fields.
		"""
		super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)

		self.fields[self.username_field] = serializers.CharField()
		self.fields['password'] = PasswordField(write_only=True)
		self.fields['remember_me'] = serializers.BooleanField(default=False)


	@property
	def username_field(self):
		return get_username_field()


	def validate(self, attrs):
		credentials = {
		    self.username_field: attrs.get(self.username_field),
		    'password': attrs.get('password')
		}

		if all(credentials.values()):
			user = authenticate(**credentials)

			if user:
				if not user.is_active:
				    msg = _('User account is disabled.')
				    raise serializers.ValidationError(msg)

				payload = jwt_payload_handler(user)

				if not attrs.get('remember_me'):
					delta = datetime.timedelta(minutes=60)
					payload['exp'] = timezone.now() + delta

				return {
				    'token': jwt_encode_handler(payload),
				    'user': user
				}
			else:
				msg = _('Unable to login with provided credentials.')
				raise serializers.ValidationError(msg)
		else:
			msg = _('Must include "{username_field}" and "password".')
			msg = msg.format(username_field=self.username_field)
		raise serializers.ValidationError(msg)
