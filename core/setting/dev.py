from core.settings import *

SECRET_KEY = "django-insecure-g(m^8r^r&!jp+bn1rdhc0q3%zak+46l7my#8d3qs%i24nhnzc*"

DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = ["127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": config("DEV_DB_ENGINE"),
        "NAME": config("DEV_DB_NAME"),
        "USER": config("DEV_DB_USER"),
        "PASSWORD": config("DEV_DB_PASSWORD"),
        "HOST": config("DEV_DB_HOST"),
        "PORT": config("DEV_DB_PORT")
    }
}

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")