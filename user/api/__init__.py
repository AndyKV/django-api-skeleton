from .user import UserCreateView, UserActivateView, UserProfileView
from .login import UserLoginView
from .password import PasswordResetView, PasswordUpdateView


__all__ = [
	'PasswordUpdateView',
	'PasswordResetView',
	'UserActivateView',
	'UserProfileView',
	'UserCreateView',
	'UserLoginView',
]
