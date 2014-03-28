"""
Django settings for {{ project_name }} project.
"""

from __future__ import with_statement
import ConfigParser
import os
import dj_database_url
import django_cache_url


# ==================================================
# Environment variables
# ==================================================

my_dir_path = os.path.dirname(os.path.abspath(__file__))
env_ini_path = os.path.join(my_dir_path, 'env.ini')

if os.path.exists(env_ini_path):
    cp = ConfigParser.SafeConfigParser()
    cp.optionxform = str

    with open(env_ini_path) as fin:
        cp.readfp(fin)

    if cp.has_section('environment'):
        for key, value in cp.items('environment'):
            os.environ[key] = value


# ==================================================
# Secret key
# ==================================================

SECRET_KEY = os.environ['SECRET_KEY']


# ==================================================
# Debug flag
# ==================================================

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']


# ==================================================
# Django applications / middlewares
# ==================================================

ADDITIONAL_INSTALLED_APPS = (
)


# ==================================================
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# ==================================================

DATABASES = {
    'default': dj_database_url.config()
}


# ==================================================
# Cache
# https://docs.djangoproject.com/en/1.6/ref/settings/#caches
# ==================================================

CACHES = {
    'default': django_cache_url.config()
}

# ==================================================
# Mail
# https://docs.djangoproject.com/en/1.6/topics/email/
# ==================================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
