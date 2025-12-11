from pathlib import Path
import os
import environ
from celery.schedules import crontab
from datetime import timedelta
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # dev uchun

AUTH_USER_MODEL = 'user.CustomUser' # custom user model

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # libs
    'drf_yasg',
    'rest_framework',
    # "corsheaders", # cors
    'query_counter', # query counter
    'rest_framework_simplejwt', # JWT auth
    # token blacklist
    'rest_framework_simplejwt.token_blacklist',

    # local apps
    'apps.weather',
    'apps.user',
    
    'apps.monitoring', # monitoring app
]

# ============================
# REDIS CACHE SETTINGS
# ============================

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"}
    }
}

# ============================
# CELERY + REDIS SETTINGS
# ============================

CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_TIMEZONE = "Asia/Tashkent"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_ACKS_LATE = True
CELERY_TASK_REJECT_ON_WORKER_LOST = True
CELERY_TASK_ALWAYS_EAGER  = False  # development uchun True qilinadi

# CELERY_BEAT_SCHEDULE Settings

CELERY_BEAT_SCHEDULE = {
    "clean-monitoring-logs": {
        "task": "apps.monitoring.tasks.clean_old_monitoring_logs",
        "schedule": crontab(minute="*/10")  # 10 minutes
    }
}

# Cors

# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # session auth ham ishlashi uchun
        'rest_framework.authentication.SessionAuthentication',
    )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # "corsheaders.middleware.CorsMiddleware", # cors
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'query_counter.middleware.DjangoQueryCounterMiddleware', # query counter
    'apps.monitoring.middleware.FullMonitoringMiddleware',  # monitoring middleware
]

# Django Query Counter Settings

DJANGO_QUERY_COUNTER = {
    'DQC_SLOWEST_COUNT': 5,
    'DQC_TABULATE_FMT': 'pretty',
    'DQC_SLOW_THRESHOLD': 1,  # seconds
    'DQC_INDENT_SQL': True,
    'DQC_PYGMENTS_STYLE': 'tango',
    'DQC_PRINT_ALL_QUERIES': False,
    'DQC_COUNT_QTY_MAP': {
        5: 'green',
        10: 'white',
        20: 'yellow',
        30: 'red',
    },
}

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/staticfiles/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/mediafiles/'

MEDIA_ROOT = BASE_DIR / 'mediafiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

### JWT Settings

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),        # Access token amal qilish vaqti
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),          # Refresh token amal qilish vaqti
    "ROTATE_REFRESH_TOKENS": False,                       # Refresh token rotation yo‘q
    "BLACKLIST_AFTER_ROTATION": False,                    # Token blacklist ishlatilmaydi
    "ALGORITHM": "HS256",                                 # Token algoritmi
    "SIGNING_KEY": settings.SECRET_KEY,                   # Django SECRET_KEY bilan imzolash
    "AUTH_HEADER_TYPES": ("Bearer",),                     # Authorization header tipi
    "USER_ID_FIELD": "id",                                # Token ichida user identifikatori
    "USER_ID_CLAIM": "user_id",                           # Token da user id field
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",)  # Token class
}

# SMTP Settings

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = "xasanbayevturdiali@gmail.com"
EMAIL_HOST_PASSWORD = "pxsu ncwd pfkh nrgp"
