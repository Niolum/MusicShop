from os import environ

from .base import *


environ.Env.read_env(str(Path(__file__).parent / ".env"), DEBUG='False')
