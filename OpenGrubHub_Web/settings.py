"""
Django settings for 454_website project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "This is a test key"  # config("SECRET_KEY")
GOOGLE_MAPS_API_KEY = config("GOOGLE_MAPS_API_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
#GDAL_LIBRARY_PATH = r'C:\Program Files\GDAL\gdal305.dll'
try:
    from osgeo import gdal
    gdal_path = Path(gdal.__file__)
    OSGEO4W = os.path.join(gdal_path.parent)
    os.environ["OSGEO4W_ROOT"] = OSGEO4W
    os.environ["GDAL_DATA"] = os.path.join(OSGEO4W, "data", "gdal")
    os.environ["PROJ_LIB"] = os.path.join(OSGEO4W, "data", "proj")
    os.environ["PATH"] = OSGEO4W + ";" + os.environ["PATH"]
    GEOS_LIBRARY_PATH = str(os.path.join(OSGEO4W, "geos_c.dll"))
    GDAL_LIBRARY_PATH = str(os.path.join(OSGEO4W, "gdal304.dll"))
except ImportError:
    GEOS_LIBRARY_PATH = None
    GDAL_LIBRARY_PATH = None
    print("error")
#GEOS_LIBRARY_PATH = r'C:\OSGeo4W\bin\geos_c.dll'


LOGIN_REDIRECT_URL = "EntryPage:hf-main-page"
LOGOUT_REDIRECT_URL = "EntryPage:hf-main-page"
LOGIN_URL = "/login"
# Application definition
# FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    "Profiles",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "django_google_maps",
    "crispy_forms",
    "star_ratings",
    "coverage",
    "phonenumber_field",
    "phonenumbers",
    ### MY APPS
    "EntryPage",
    "OpenGrubHub_Web",
    "FileUpload",
    "ReservationApp",
    "RestaurantFinder",
    "Community",
    "Table",
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "OpenGrubHub_Web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "EntryPage", "templates"),
            os.path.join(BASE_DIR, "Profiles", "templates"),
            os.path.join(BASE_DIR, "FileUpload", "templates"),
            os.path.join(BASE_DIR, "ReservationApp", "templates"),
            os.path.join(BASE_DIR, "RestaurantFinder", "templates"),
            os.path.join(BASE_DIR, "Community","templates"),
            os.path.join(BASE_DIR,"Table","templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
#STAR_RATINGS_RERATE = False
WSGI_APPLICATION = "OpenGrubHub_Web.wsgi.application"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "Profiles.User"
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
GEOIP_PATH = os.path.join(BASE_DIR, 'geoip')

TIME_INPUT_FORMATS = ['%I:%M %p',]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "ReservationApp/static",
    BASE_DIR / "RestaurantFinder/static",
    BASE_DIR / "EntryPage/static",
    BASE_DIR / "Profiles/static",
    BASE_DIR / "Community/static",
    BASE_DIR / "Table/static",
    str(BASE_DIR.joinpath('static')),
]

STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_FINDERS = [
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# only if django version >= 3.0
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]