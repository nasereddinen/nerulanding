import os
import django_heroku
from django.utils.log import DEFAULT_LOGGING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_HOSTCONF = 'getdinerotoday.hosts'
DEFAULT_HOST = 'www'
ROOT_URLCONF = 'getdinerotoday.urls'
LOGIN_URL = '/user/login'
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
CORS_ORIGIN_ALLOW_ALL = True
WSGI_APPLICATION = 'getdinerotoday.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEBUG = False
X_FRAME_OPTIONS = 'SameOrigin'
SECURE_REFERRER_POLICY = 'strict-origin'
EMAIL_BACKEND = 'django_amazon_ses.EmailBackend'
AWS_DEFAULT_REGION = 'us-east-1'
DEFAULT_FROM_EMAIL = 'info@kleui.com'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
AWS_ACCESS_KEY_ID = "AKIA2T2OGYUW3Q4XDGG7"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = 'kleui-up'
AWS_S3_REGION_NAME = 'us-east-1'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = None


DEFAULT_LOGGING['handlers']['console']['filters'] = []

INSTALLED_APPS = [
    'django_hosts',
    'rest_framework',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_extensions',
    'user',
    'business',
    'bcbsoftwares',
    'financing_portal',
    'portals.cannabis',
    'portals.fitness',
    'portals.insurance_agent',
    'portals.musician',
    'portals.restaurant_catering',
    'portals.wedding_planner',
    'portals.accountant',
    'portals.credit_repair',
    'portals.hair_salon',
    'portals.lawyer',
    'portals.photography',
    'portals.transportation',
    'portals.automotive',
    'portals.ecommerce',
    'portals.handy_man',
    'portals.medical',
    'portals.real_estate',
    'portals.construction',
    'portals.trucking',
    'import_export',
    'loanportal',
    'businesscreditcourse',
    'marketingcourse',
    'yourplan',
    'whitelabelpartnerportal',
    'creditcourse',
    'covid19',

    'affiliate',
    'storages',
    'goals',
    'products',
    'onlinetools',
    'dynamic',
    'orders',
    'chromeextension',
    'onboarding',
    'banking',
    'freewhitelabelprogramonboarding',
    'corsheaders',
]

MIDDLEWARE = [
    'getdinerotoday.middleware.hosts.HostsRequestMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'getdinerotoday.middleware.hosts.HostsResponseMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), 'user/templates', 'business/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'getdinerotoday.contexts.ProfileProcessor',
                'getdinerotoday.contexts.whitelabel_processor',

            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication'],

}
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Activate Django-Heroku.

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())
