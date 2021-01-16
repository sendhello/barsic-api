import os

import environ

root = environ.Path(__file__) - 3  # get root of the project
env = environ.Env()
environ.Env.read_env()  # reading .env file
public_root = root.path('public/')

SITE_ROOT = root()

# SECRET_KEY=django
SECRET_KEY = env.str('SECRET_KEY', default='django')

# DEBUG=True
DEBUG = env.bool('DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG

# ALLOWED_HOSTS=127.0.0.1:192.168.1.1
ALLOWED_HOSTS = env.str('ALLOWED_HOSTS', default='*').split(':')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'solo.apps.SoloAppConfig',
    'rest_framework',
    'api',
    'settings'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {'default': env.db('DATABASE_URL', default="sqlite:///data.db")}

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

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = public_root('static')
STATIC_URL = env.str('STATIC_URL', default='static/')
STATICFILES_DIRS = [
    os.path.join(SITE_ROOT, 'static'),
]

MEDIA_ROOT = public_root('media')
MEDIA_URL = env.str('MEDIA_URL', default='media/')

# CACHES = {'default': env.cache('REDIS_CACHE_URL')}

# GET_PARAM_DB = 'db'

# ADMINS=admin::admin1234,vasya:vasya@mail.ru:vasya123
ADMINS = env.str('ADMINS', default='admin::admin1234')
