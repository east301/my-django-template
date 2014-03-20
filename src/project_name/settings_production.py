"""
Django settings for {{ project_name }} project.
"""

import os
import dj_database_url
import django_cache_url


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
