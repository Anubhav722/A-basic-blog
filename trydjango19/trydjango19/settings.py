"""
Django settings for trydjango19 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os # OS is a pytohn module that allows us to use cross platform functionality for finding path to directories and files.
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # we are finding the path for our base directory. it aviods hard coding and saves us time..in this case our BASE_DIR is trydjango19(outer)
# print BASE_DIR    prints location of BASE_DIR 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n#esg3zw0p04@*)rcw02@v=9lyz62hp-m5z7d=_dijhufao2=o' #protects when we are running sessions, messages, passwords reset...should never be shared with anybody...when we create our it is generated automatically 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True# must not be true during production only during development... never leave it on when launching ..responsible for giving the errors

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [] # when the DEBUG is set to false protects against HTTP host header attacks --means someone coming over and changing it over o differnt domain name...
# when the DEBUG=False, we set our domain name for eg. ALLOWED_HOSTS=['.learnpythontutorial.com']-- this is not required during development

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
)

MIDDLEWARE_CLASSES = ( #they are lightweight software that handles request and response to from our client(user) to server .. when the client goes to website and they request something and oln this server sends back to the website ..that's response
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'trydjango19.urls' # this is how we handle request, how we grab the request from the user.. it is actually a path to our main urls file

WSGI_APPLICATION = 'trydjango19.wsgi.application' #this is the path to our development server, the one we randomly run "python manage.py runserver".. this is the path to that server


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # our path to database
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'#language        

TIME_ZONE = 'UTC' #time zone

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/' #static files where they are going to be located and how we are going to handle them


TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)


STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static' ),
    ]
#STATIC_ROOT=os.path.join{os.path.join((BASE_DIR), 'static_cdn'))    
#STATIC_ROOT=os.path.join((BASE_DIR), 'static_cdn')
#static_cdn is in a content delivery network like if you were emulating our static files being on a differnet server
STATIC_ROOT=os.path.join(BASE_DIR, 'static_cdn')

MEDIA_URL='/media/'
#MEDIA_ROOT=os.path.join((BASE_DIR), 'media_cdn')
MEDIA_ROOT=os.path.join(BASE_DIR, 'media_cdn')
#MEDIA_ROOT=os.path.join(os.path.join((BASE_DIR), 'media_cdn'))


TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ]
                }
    }
    ] #extras in django 1.9
