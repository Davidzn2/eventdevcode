from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eventusdb',
        'USER':'eventususer',
        'PASSWORD':'12341234',
        'HOST':'localhost',
        'PORT':'5432',

    }
}

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')