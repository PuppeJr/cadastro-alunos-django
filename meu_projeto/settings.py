# meu_projeto/settings.py

import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta (já existe, mantenha a sua)
SECRET_KEY = '...'

# Modo DEBUG (True em desenvolvimento)
DEBUG = True

# Hosts permitidos (em desenvolvimento pode ficar vazio ou com '*')
ALLOWED_HOSTS = []

# --- APLICATIVOS INSTALADOS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'alunos',      # <-- ADICIONAMOS A NOSSA APP
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

ROOT_URLCONF = 'meu_projeto.urls'

# --- CONFIGURAÇÃO DE TEMPLATES ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Pode deixar vazio, pois usaremos pastas dentro de cada app
        'APP_DIRS': True,  # Importante: permite que o Django busque templates em cada app
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

WSGI_APPLICATION = 'meu_projeto.wsgi.application'

# --- BANCO DE DADOS (SQLite padrão) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validação de senhas (não alteramos)
AUTH_PASSWORD_VALIDATORS = []

# Internacionalização
LANGUAGE_CODE = 'pt-br'           # <-- ALTERADO PARA PORTUGUÊS
TIME_ZONE = 'America/Sao_Paulo'   # <-- ALTERADO
USE_I18N = True
USE_TZ = True

# Arquivos estáticos (CSS, JS, imagens)
STATIC_URL = 'static/'

# Campo padrão para chaves primárias
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'