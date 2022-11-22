#운영용 세팅
from .common import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME":os.getenv("DB_NAME"),
        "USER": "root",
        "PASSWORD":os.getenv("DB_PWD"),
        "HOST": "localhost",
        "PORT": "3306",
    }
}