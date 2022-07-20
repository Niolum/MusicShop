import environ


environ.Env.read_env(DEBUG='True')


from .base import *

ALLOWED_HOSTS += ['127.0.0.1',]

INSTALLED_APPS += [
    'debug_toolbar', 
]

MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
]