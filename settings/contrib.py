import datetime
import environ


env = environ.Env(DEBUG=(bool, False),)

FEATURES = env.tuple('FEATURES', default=())

RAVEN_CONFIG = {
    'dsn': 'https://d316d2206c104c62b46fb1b9595755be:ca2ca5a5bc81485f8b332263d706d4da@sentry.inprogress.rocks/8'
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
}

if 'SWAGGER' in FEATURES:
	SWAGGER_SETTINGS = { 
        'LOGIN_URL': 'admin:login',
        'LOGOUT_URL': 'admin:logout',
        'USE_SESSION_AUTH': False,
        'SHOW_REQUEST_HEADERS': True,
        'DOC_EXPANSION': 'list',
        'APIS_SORTER': 'alpha',
    }

#Celery settings
BROKER_URL = 'redis://{}:6379/0'.format(env('REDIS_HOST'))
CELERY_RESULT_SERIALIZER = 'json'

from celery.schedules import crontab


# CELERYBEAT_SCHEDULE = {
#     'task-name': {
#         'task': 'task',
#         'schedule': crontab(minute=0, hour=0),
#     },
# }
