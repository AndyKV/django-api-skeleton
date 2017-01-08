from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView, UpdateAPIView

from user.models import UserProfile
from user.serializers import PasswordUpdateSerializer, PasswordResetSerializer


class PasswordResetView(GenericAPIView):
	permission_classes = [AllowAny]
	serializer_class = PasswordResetSerializer


	def post(self, *args, **kwargs):

		serializer = self.get_serializer(data=self.request.data)

		if not serializer.is_valid():
			return Response(serializer.errors, status=400)
		
		return Response('Success')


class PasswordUpdateView(UpdateAPIView):
	serializer_class = PasswordUpdateSerializer
	permission_classes = [AllowAny]
	queryset=UserProfile.objects.all()
	lookup_field = 'token'
	http_method_names = ['patch']
