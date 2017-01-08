from rest_framework import serializers
from user.models import UserProfile


class PasswordResetSerializer(serializers.Serializer):
	email = serializers.EmailField(required=True)


	def validate(self, attrs):
		email = attrs.get('email')
		user = UserProfile.objects.get(email=email)

		if user:
			
			user.token = user.make_confirm_token()
			user.save()
			user.send_reset_password_mail.delay(user.email, user.token)
			return user

		msg = 'No user with such email'
		raise serializers.ValidationError(msg)


class PasswordUpdateSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, max_length=255, 
    						trim_whitespace=False, write_only=True)

    def save(self):
        self.instance.set_password(self.validated_data['password'])
        self.instance.save()
        return self.instance
