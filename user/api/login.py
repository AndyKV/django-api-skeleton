from rest_framework.permissions import AllowAny
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework import status

from user.serializers import JSONWebTokenSerializer


class UserLoginView(JSONWebTokenAPIView):
	serializer_class = JSONWebTokenSerializer
	permission_classes = [AllowAny]


	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)

		if serializer.is_valid():
			user = serializer.object.get('user') or request.user
			token = serializer.object.get('token')

			response_data = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER(token, user, request)
			return Response(data=response_data, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
