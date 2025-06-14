"""
Настройки проекта BotHubUz
"""

import os

# Базовая директория проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Секретный ключ Django
SECRET_KEY = 'your-secret-key'

# Режим отладки (DEBUG = True — для разработки)
DEBUG = True

# Разрешённые хосты для доступа к серверу
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Приложения, которые будут использоваться
INSTALLED_APPS = [
    # Стандартные приложения Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Локальные приложения BotHubUz
    'bots.apps.BotsConfig',  # Приложение ботов
    'users.apps.UsersConfig',  # Кастомная модель пользователя
]

# Middleware — обработка входящих запросов
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Точка входа для URL-маршрутов
ROOT_URLCONF = 'bothub_project.urls'

# Настройки шаблонизатора Django
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

# WSGI-точка входа
WSGI_APPLICATION = 'bothub_project.wsgi.application'

# Настройки базы данных PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bothub',
        'USER': 'admin',
        'PASSWORD': 'admin123',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Язык проекта
LANGUAGE_CODE = 'en-us'

# Часовой пояс
TIME_ZONE = 'UTC'

# Использовать ли локализацию
USE_I18N = True

# Использовать ли часовые пояса
USE_TZ = True

# URL для статических файлов
STATIC_URL = '/static/'

# Автоматическое создание первичных ключей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Используем кастомную модель пользователя
AUTH_USER_MODEL = 'users.User'