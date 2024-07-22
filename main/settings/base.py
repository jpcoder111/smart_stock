from pathlib import Path
import os
import json
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x5qfw9ybz8^f(wap6+=fh5i_n(5y8nmv9=ozze&#p!!k-yznv$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.webhooks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'main.middlewares.http_requests.LogRequestResponseMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# class JsonFormatter(logging.Formatter):
#     # def format(self, record):
#     #     log_record = {
#     #         'timestamp': self.formatTime(record, self.datefmt),
#     #         'level': record.levelname,
#     #         'event': record.msg.get('event', 'unknown'),
#     #         'method': record.msg.get('method', None),
#     #         'path': record.msg.get('path', None),
#     #         'headers': record.msg.get('headers', None),
#     #         'query_params': record.msg.get('query_params', None),
#     #         'body': record.msg.get('body', None),
#     #         'status_code': record.msg.get('status_code', None),
#     #         'data_type': record.msg.get('data_type', None),
#     #         'data_content': record.msg.get('data_content', None),
#     #     }
#     #     return json.dumps(log_record)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            'format': '{ "timestamp": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s }',
        },
    },
    'handlers': {
        'requests_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/http_requests/requests.log',
            'formatter': 'json',
        },
        'responses_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/http_requests/responses.log',
            'formatter': 'json',
        },
    },
    'loggers': {
        'http_requests.request': {
            'handlers': ['requests_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'http_requests.response': {
            'handlers': ['responses_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
