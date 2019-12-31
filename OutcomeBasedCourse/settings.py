import os
from .config.martor import *

# from .config.djmoney_config import *

import ldap
from django_auth_ldap.config import (
    LDAPSearch,
    PosixGroupType,
)  # GroupOfNamesType


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "k01@s%35uz)2un(s63l^&mj1504=g5f#4*@hj2=5j($dawaokx"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ldap config start

# Baseline configuration.
# ldaps protocol specify here ldap + tls
AUTH_LDAP_SERVER_URI = "ldaps://lab.gdy.club:389"
AUTH_LDAP_START_TLS = True

AUTH_LDAP_BIND_DN = "cn=admin,dc=lab,dc=gdy,dc=club"
AUTH_LDAP_BIND_PASSWORD = "fillpassword"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "dc=lab,dc=gdy,dc=club", ldap.SCOPE_SUBTREE, "(cn=%(user)s)"
)
# Or:
AUTH_LDAP_USER_DN_TEMPLATE = "cn=%(user)s,ou=users,dc=lab,dc=gdy,dc=club"

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "ou=groups,dc=lab,dc=gdy,dc=club",
    ldap.SCOPE_SUBTREE,
    "(objectClass=posixGroup)",
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr="cn")

# Simple group restrictions
AUTH_LDAP_REQUIRE_GROUP = "cn=admins,ou=groups,dc=lab,dc=gdy,dc=club"
AUTH_LDAP_DENY_GROUP = None  #'cn=users,ou=groups,dc=lab,dc=gdy,dc=club'

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    #    'email': 'mail',
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=admins,ou=groups,dc=lab,dc=gdy,dc=club",
    "is_staff": "cn=admins,ou=groups,dc=lab,dc=gdy,dc=club",
    "is_superuser": "cn=admins,ou=groups,dc=lab,dc=gdy,dc=club",
}
#
# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache distinguished names and group memberships for an hour to minimize
# LDAP traffic.
AUTH_LDAP_CACHE_TIMEOUT = 0

# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)

# ldap config end

LOGIN_URL = '/admin/login'

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_tables2",
    "bootstrap4",
    "crispy_forms",
    "martor",
    # "djmoney",
    "course.apps.CourseConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "OutcomeBasedCourse.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "OutcomeBasedCourse.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "outcomebasedcourse",
        "HOST": "localhost",
        "PORT": "",
        "USER": "outcomebasedcourse",
        "PASSWORD": "outcomebasedcourse",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {
        "django_auth_ldap": {"level": "DEBUG", "handlers": ["console"]}
    },
}


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
