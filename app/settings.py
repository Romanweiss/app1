"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

# импорт библиотеки для удобной работы с путями расположения
from pathlib import Path

from django.conf.global_settings import LOGIN_URL, MEDIA_ROOT, MEDIA_URL


# Путь, который ведёт к корневому каталогу нашего проекта - BASE_DIR
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7qfz&=qvrzzf6mqe)fwu0%ef%ay(!b)e_d0+qe5a9)k_l(ydtk'

# переменная для вывода отладочной информации
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # хосты для приложения '*' - для любых хостов


# Application definition
# cписок приложений - в нём регистрируем новые приложения!
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # приложение для поиска и обслуживания статических файлов
    'django.contrib.postgres',  # подключаем для поиска

    'debug_toolbar', # приложение - тулбар для отслеживания sql запросов прямо на сайте

    'main', # регистрируем основное приложение
    'goods',
    'users',
    'carts',
    'orders',
]

# промежуточные слои(программное обеспечение) отвечающие за безопасность, аутентификацию, обработку файлов куки итд
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',  # для дебаг тулбара
]

# указатель на url адреса нашего приложения
ROOT_URLCONF = 'app.urls'

# настройки шаблонизатора
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # для шаблонов, которые используются во всех приложениях
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# подключение базы данных и настройка
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3', # - бд по умолчанию
        #'NAME': BASE_DIR / 'db.sqlite3', # атрибуты по умолчанию

        # - подключаем postgresql
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'home',
        'USER': 'home',
        'PASSWORD': '694520',
        'HOST': 'localhost',
        'PORT': '5432',
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
# валидаторы паролей
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# префикс для url адреса статики
STATIC_URL = 'static/'


# папка для статики в корне, путь указываем по схеме выше. общая статика, которая применима для всех приложений
STATICFILES_DIRS = [BASE_DIR / 'static',]

# название url префикса для media
MEDIA_URL = 'media/'

# здесь джанго будет искать медиа файлы
MEDIA_ROOT = BASE_DIR / 'media'

# также требуется для sql дебагера
INTERNAL_IPS = ["127.0.0.1",]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # автоматическая инкрементация для id

# переопределение стандартной модели на нашу (расширение функционала - добавлен аватар)
AUTH_USER_MODEL = 'users.User'

# переопределение адреса страницы логина (изначально - accounts/login)
LOGIN_URL = '/user/login/'
