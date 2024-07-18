from core.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS')


DATABASES = {
    "default": {
        "ENGINE": config("PROD_DB_ENGINE"),
        "NAME": config("PROD_DB_NAME"),
        "USER": config("PROD_DB_USER"),
        "PASSWORD": config("PROD_DB_PASSWORD"),
        "HOST": config("PROD_DB_HOST"),
        "PORT": config("PROD_DB_PORT")
    }
}