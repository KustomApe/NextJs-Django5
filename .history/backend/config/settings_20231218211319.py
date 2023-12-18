import os
import environ

from pathlib import Path
from datetime import timedelta
from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = 'django-insecure-j4(m4z$f*q2j%c%zl&1%7lii&jj*vpj07vzdr%*ds#hfmf^f=@'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'accounts',
    'cloudinary',
    'cloudinary_storage',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
# Production envではCORS_ALLOWED_ORIGINSを指定する
# CORS_ALLOWED_ORIGINS = []

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

default_dburl = 'sqlite:///' + str(BASE_DIR / 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl)
}


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


LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = str(BASE_DIR / 'staticfiles')

MEDIA_URL = '/media/'

# Cloudinaryを使用
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MEdiaCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_NAME'),
    'API_KEY': env('CLOUDINARY_API_KEY'),
    'API_SECRET': env('CLOUDINARY_API_SECRET'),
}

# メール設定
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# Rest Framework設定
REST_FRAMEWORK = {
    # 認証が必要
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framwork.permissions,IsAuthenticated',
    ],
    # JWT認証
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framwork_simplejwt.authentication.JWTAuthentication',
    ],
    # 日付
    'DATETIME_FORMAT': '%Y%m%d %H%M',
}

# JWT設定
SIMPLE_JWT = {
    # アクセストークン(1day)
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    # リフレッシュトークン(5days)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    # 認証タイプ
    'AUTH_TOKEN_CLASSES': ('rest_framwork_simplejwt.tokens.AccessToken',),
    # 認証トークン
}
