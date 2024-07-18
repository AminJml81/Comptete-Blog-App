from core.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS')


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

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