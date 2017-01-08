from django.conf.urls import url

from .api import (
	UserLoginView,
	UserCreateView,
	UserProfileView,
	UserActivateView,
	PasswordResetView, 
	PasswordUpdateView,
)


urlpatterns = [
	url(r'^users/profile/$', UserProfileView.as_view(), name='user-profile'),
	url(r'^login/$', UserLoginView.as_view(), name='login'),
	url(r'^users/$', UserCreateView.as_view(), name='register'),
	url(r'^users/password/reset/$', PasswordResetView.as_view(), name='reset_password'),
	url(r'^users/activate/(?P<token>[\w-]+)/$', UserActivateView.as_view(), name='activate_user'),
	url(r'^users/password/update/(?P<token>[\w-]+)/$', PasswordUpdateView.as_view(), name='update_password'),	
]
