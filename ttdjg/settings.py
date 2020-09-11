"""
Django settings for ttdjg project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jp6p^o4_t*t$f493k=)g-ml12w$-4&tl(h=90idx7&5(%yl_&^'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
# ALLOWED_HOSTS = ['*']

DEBUG = True
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'ttdjg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # "django.core.context_processors.i18n"
            ],
        },
    },
]

WSGI_APPLICATION = 'ttdjg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_web',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

STATIC_ROOT = os.path.join(BASE_DIR, "static")

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = 'localhost'
SESSION_PORT = '6397'
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = 'week'
SESSION_REDIS_PREFIX = 'session'


# simple-ui
SIMPLEUI_ANALYSIS = False
SIMPLEUI_STATIC_OFFLINE = True

SIMPLEUI_DEFAULT_ICON = False

# SIMPLEUI_ICON={
#     # 'Bloggers':'fab fa-blogger',
#     # 'Layouts':'fab fa-themeisle',
#     # 'Links':'fas fa-link',
#     # 'Posts':'fas fa-book',
#     # 'Comments':'far fa-comments',
#     # 'Categorys':'fas fa-tags'
# }

# SIMPLEUI_HOME_PAGE
# SIMPLEUI_HOME_TITLE
# SIMPLEUI_HOME_ICON
# SIMPLEUI_DEFAULT_ICON
# SIMPLEUI_ICON
# SIMPLEUI_ANALYSIS


# SIMPLEUI_ICON={
#     'My_App':'fab fa-blogger',
# }

# SIMPLEUI_HOME_ACTION = False #最近动作

# LOCALE_PATHS = (
#     os.path.join(BASE_DIR, 'locale'),
# )

# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.core.context_processors.i18n",
# )

