from os import environ

from .base import *


environ.Env.read_env(str(Path(__file__).parent / ".env"), DEBUG='False')

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'