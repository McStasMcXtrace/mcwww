"""
Django settings for mcweb project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os
import ldap
from django_auth_ldap.config import LDAPSearch

# --- START Deployment configuration ---

MCWEB_LDAP_DN = 'dc=risoe,dc=dk'

AUTH_LDAP_SERVER_URI = "ldap://localhost"
AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,%s" % MCWEB_LDAP_DN, ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    #'django.contrib.auth.backends.ModelBackend', # uncomment this line to enable local sign-on (django-db)
)

# number of MPI processes pr worker process
MPI_PR_WORKER=10

# mcplot configuration
#  For Python + Gnuplot use 
#MCPLOT_CMD = "mcplot-gnuplot-py -s"
#MCPLOT_LOGCMD = "mcplot-gnuplot-py -s -l"
#  For Perl + PGPLOT use
MCPLOT_CMD = "mcplot -png"
MCPLOT_LOGCMD = "mcplot -png -log"

# Use aopt from instantReality (http://www.instantreality.org)
USE_AOPT = True
AOPT_CMD = "aopt.sh"

# list of courses for signupper - each entry will appear as a checkbox when generating
# the signup form using the command "python manage.py signupform"
COURSES = [
    'intro-ns-selfstudy', 
    'intro-ns',
    'musr', 
    ]
# all users will be enrolled in these:
COURSES_MANDATORY = [
    'lib',
    'quiz-taster',
    ]

# used by uploader, NOTE: must not be empty (in which case the uploader will not work)
FILE_UPLOAD_PW = 'upload123'

# --- END Deployment configuration ---

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# folder containing subfolders (aka "groups") containing instruments
SIM_DIR = os.path.join(BASE_DIR, 'sim')

# data dir is located within static root
DATA_DIRNAME = 'data'

# applied as mcrun -d parameter in runworker
MCRUN_OUTPUT_DIRNAME = 'mcstas'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xne_dc*7f3#q(l*c1a97v@q!g$myz@4lcwt5ij&wx7t4)e+b5k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['mcstas-01.risoe.dk', 'e-neutrons.org', 'sim.e-neutrons.org']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simrunner',
    'signupper',
    'uploader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mcweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'simrunner/templates', 
            'signupper/templates',
            'uploader/templates',
        ],
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

WSGI_APPLICATION = 'mcweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
