"""
Django settings for {{ project_name }} project.
"""

import os
import dj_database_url
import django_cache_url


# ==================================================
# Project path
# ==================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ==================================================
# Secret key
# ==================================================

SECRET_KEY = '{{ secret_key }}'


# ==================================================
# Debug flag
# ==================================================

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']


# ==================================================
# Django applications / middlewares
# ==================================================

ADDITIONAL_INSTALLED_APPS = (
    'debug_toolbar',
)


# ==================================================
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# ==================================================

DATABASES = {
    'default': dj_database_url.parse('sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
}


# ==================================================
# Cache
# https://docs.djangoproject.com/en/1.6/ref/settings/#caches
# ==================================================

CACHES = {
    'default': django_cache_url.parse('locmem://')
}


# ==================================================
# Mail
# https://docs.djangoproject.com/en/1.6/topics/email/
# ==================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
