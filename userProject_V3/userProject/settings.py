"""
Django settings for userProject project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd7k+ilw-)h$__1-eww=)ec5!dcz0&0bd180_f91_10fym51910'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1','mysite.com']

# ALLOWED_HOSTS = ['localhost', '127.0.0.1','mysite.com']

# Application definition

INSTALLED_APPS = [
    'userProfile', #app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms', # crispy form
    'social_django',  # <-- #social app  # pip install social-auth-app-django
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    'social_django.middleware.SocialAuthExceptionMiddleware',  # <--
]

ROOT_URLCONF = 'userProject.urls'

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

WSGI_APPLICATION = 'userProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles")
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# image path
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Bootstrap4 crispy form
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# During development only
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  


# sending mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'azizur.rahman363410@gmail.com'
EMAIL_HOST_PASSWORD = 'zbatpattgnwustjt'


# python-social-auth settings
AUTHENTICATION_BACKENDS = (
   'social_core.backends.github.GithubOAuth2',      # <-- Github
   'social_core.backends.twitter.TwitterOAuth',     # <-- Tweeter
   'social_core.backends.facebook.FacebookOAuth2',  # <--  Facebook
    'social_core.backends.google.GoogleOAuth2',     #<-- google +

#for email backend
    'django.contrib.auth.backends.ModelBackend',
    'userProfile.authentication.EmailAuthBackend',
)

# SOCIAL_AUTH_GITHUB_KEY = '44fd4145a8d85fda4ff1'
# SOCIAL_AUTH_GITHUB_SECRET = '2de7904bdefe32d315805d3b7daec7906cc0e9e7'

# SOCIAL_AUTH_FACEBOOK_KEY = '426689634898716'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'c8884f1bdc8d7c93f5430ecb9073e8a3'

SOCIAL_AUTH_TWITTER_KEY = '9TD12xahCWCDdyLzpmw61GSM9'
SOCIAL_AUTH_TWITTER_SECRET = 'mwtdcUe4uOvvJjDk2AuQ9Mq2xiHPw3740m5iGLf6hwg3B4TNSx'

# mine

# for Facebook+
SOCIAL_AUTH_FACEBOOK_KEY = '451821651x33143'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '524fada3c3ca5adgb279da535da1d863'  # App Secret


# for Github+
SOCIAL_AUTH_GITHUB_KEY = 'Iv1.992b71a64e5f2633'
SOCIAL_AUTH_GITHUB_SECRET = '3c38a23146cbdcc983a9a5138e36c4f089960f1a'

# for google+
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '971897068464-81u76n5ivfpkb7e15h3vk17qtjq4k7gf.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ISM6Q5JfCc8H0mQP64yMVzDZ'