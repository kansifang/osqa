# encoding:utf-8
# Django settings for lanai project.
import os.path
from django.conf import global_settings

SITE_ID = 1

SERVE_MEDIA = True

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/forum/admin/media/'
SECRET_KEY = '$oo^&_m&qwbib=(_4m_n*zn-d=g#s0he5fx9xonnym#8p6yigm'
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (   
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    #'django.middleware.sqlprint.SqlPrintingMiddleware',
    'middleware.anon_user.ConnectToSessionMessagesMiddleware',
    'middleware.pagesize.QuestionsPageSizeMiddleware',
    'middleware.cancel.CancelActionMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.doc.XViewMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    #'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'context_processors.settings',
    #'django.core.context_processors.i18n',
    'user_messages.context_processors.user_messages',#must be before auth
    'django.core.context_processors.auth', #this is required for admin
    #'cnprog.context_processors.auth_processor', #this one unfortunately breaks admin interface
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django_extensions',
    'profiles',
    'django_authopenid',
    'djangosphinx',
    'forum',
    #'debug_toolbar' ,
    'user_messages',
)

<<<<<<< HEAD:settings.py
# User settings
from settings_local import *
