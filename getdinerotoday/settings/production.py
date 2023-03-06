import dj_database_url

from getdinerotoday.settings.settings import *

DEBUG = False

SECRET_KEY = os.environ.get(
    'SECRET_KEY', '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki')

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication'],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}
STRIPE_PUBLISHABLE_KEY = "pk_live_51MKgjLKFzQhQect9F0Wfd5w694fA27RyW6TJN8ISRqQkpsqrtP3dsyXxVlR6jRia86IA5wGHPks4oLt3rD4vXW0G00SJAjb5MQ"

STRIPE_SECRET_KEY = "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"

ALLOWED_HOSTS = ['*']
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

