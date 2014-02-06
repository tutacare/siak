# -*- coding: utf-8 -*-

import os

my_make_path = lambda x: "%s/%s" % (os.path.dirname(os.path.dirname(os.path.realpath(__file__))), x)
MY_PROJECT = __package__

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'your_database',
		'USER' : 'root',
		'PASSWORD': 'your_password'
    }
}

TIME_ZONE = 'Asia/Jakarta'
LANGUAGE_CODE = 'id'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = my_make_path('media')
MEDIA_URL = '/media/'
STATIC_ROOT = my_make_path('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (my_make_path('siak/static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

SECRET_KEY = 'xnq9p82muz98qm9pe839r8heiuf'

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    #'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'siak',
)

ROOT_URLCONF = MY_PROJECT + '.urls'

WSGI_APPLICATION = MY_PROJECT + '.wsgi.application'

TEMPLATE_DIRS = (
    my_make_path('templates/siak'),
)

DIRECTORY = 'uploads/'

EMAIL_FROM = 'ayes.email@gmail.com'
EMAIL_TO = 'ayes.email@gmail.com'