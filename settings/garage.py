import environ


env = environ.Env()
root = environ.Path(__file__) - 2
SITE_ROOT = root()

DEBUG = env('DEBUG', default=False)

# Pagination
DEFAULT_PAGE_ORDERS = 10

DEFAULT_EMAIL = 'email@test.com'
EMAIL_REGISTRATION_TITLE = 'API Registration'
EMAIL_PASSWORD_RESET_TITLE = 'API Password Reset'


# MAILGUN_SERVER_NAME = ''
# MAILGUN_ACCESS_KEY = ''
# EMAIL_BACKEND = ''


# if DEBUG:
# 	EMAIL_HOST = ''
# 	EMAIL_PORT = 587
# 	EMAIL_HOST_USER = ''
# 	EMAIL_HOST_PASSWORD = ''
