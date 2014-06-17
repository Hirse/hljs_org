import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'highlightjs.org']
ADMINS = [('Ivan Sagalaev', 'maniac@softwaremaniacs.org')]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hljs_org',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hljs_org.urls'
WSGI_APPLICATION = 'hljs_org.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hljs_org',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = False
USE_L10N = False
USE_TZ = True

STATIC_URL = '/static/'

## Custom settings

HLJS_SOURCE = '<undefined>'
HLJS_CACHE = '<undefined>'
HLJS_TOUCHFILE = '<undefined>'
HLJS_CODESTYLES = [
    'default',
    'solarized_dark',
    'solarized_light',
    'github',
    'railscasts',
    'monokai_sublime',
    'mono-blue',
]
HLJS_CDNS = [
    (
        'cdnjs',
        'http://cdnjs.cloudflare.com/ajax/libs/highlight.js/%s/highlight.min.js',
        'http://cdnjs.cloudflare.com/ajax/libs/highlight.js/%s/styles/default.min.css',
    ),
    (
        'Yandex',
        'http://yandex.st/highlightjs/%s/highlight.min.js',
        'http://yandex.st/highlightjs/%s/styles/default.min.css',
    ),
]
