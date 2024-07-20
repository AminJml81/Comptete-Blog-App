from core.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = [config('ALLOWED_HOSTS')]


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

X_FRAME_OPTIONS = "SAMEORIGIN"

CSRF_COOKIE_SECURE = True

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# more security settings
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "SAMEORIGIN"
SECURE_REFERRER_POLICY = "strict-origin"
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")