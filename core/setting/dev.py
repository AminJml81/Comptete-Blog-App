from core.settings import *

SECRET_KEY = "django-insecure-g(m^8r^r&!jp+bn1rdhc0q3%zak+46l7my#8d3qs%i24nhnzc*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

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