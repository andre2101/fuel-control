# -*- coding: utf-8 -*-
import os
from S3 import CallingFormat

SECRET_KEY = 'wu!4+o&l%4r7r%vn7z7^1ifbku5n&u=_bfgjiom87&0d25nlhu'

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
LOCAL = lambda x: os.path.join(SITE_ROOT, x)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Victor Fontes', 'contato@sparkit.com.br')
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': LOCAL('db.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'

USE_I18N = True
USE_L10N = True

SITE_ID = 1

ON_HEROKU = os.environ.has_key('DATABASE_URL')

if ON_HEROKU:
    AWS_ACCESS_KEY_ID = 'AKIAJ6C7XWK5CTIAMC7A'
    AWS_SECRET_ACCESS_KEY = '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'
    S3_FILE_STORAGE = 'storages.backends.s3.S3Storage'
    AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
    AWS_S3_SECURE_URLS = True
    STATICFILES_STORAGE = S3_FILE_STORAGE
    DEFAULT_FILE_STORAGE = S3_FILE_STORAGE

    AWS_STORAGE_BUCKET_NAME = 'fuel-control'

    #STATIC_ROOT = '/'
    STATIC_ROOT = ''
    STATIC_URL = 'https://s3-sa-east-1.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #EMAIL_BACKEND = 'django_mailer.smtp_queue.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

else:
    STATIC_ROOT = LOCAL('static_root')
    STATIC_URL = '/static/'
    ADMIN_MEDIA_PREFIX = '/static/admin/'




MEDIA_ROOT = LOCAL('media')
MEDIA_URL = '/media/'

    

STATICFILES_DIRS = (
    LOCAL('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    
    # required by django-admin-tools
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'fuelcontrol.urls'

TEMPLATE_DIRS = (LOCAL('templates'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'cars',
    'fuels',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}