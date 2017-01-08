from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, UpdateAPIView

from user.models import UserProfile
from user.serializers import UserSerializer, ActivateUserSerializer


class UserCreateView(CreateAPIView):
	permission_classes = [AllowAny]
	serializer_class = UserSerializer


class UserActivateView(UpdateAPIView):
	permission_classes = [AllowAny]
	serializer_class = ActivateUserSerializer
	queryset=UserProfile.objects.all()
	lookup_field = 'token'
	http_method_names = ['patch']


class UserProfileView(APIView):
	serializer_class = UserSerializer


	def get(self, request, format=None):
		serializer = self.serializer_class(request.user)
		return Response(data=serializer.data, status=200)
