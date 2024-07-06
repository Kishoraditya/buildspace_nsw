from .base import *
import dj_database_url
import os

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
# Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#import environ

#env = environ.Env()
#environ.Env.read_env()  # reads the .env file

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': env('DB_NAME'),
#        'USER': env('DB_USER'),
##        'PASSWORD': env('DB_PASSWORD'),
#        'HOST': env('DB_HOST'),
#        'PORT': env('DB_PORT'),
#    }
#}

#import os
#import dj_database_url

# ... other settings ...

#DATABASES = {
#    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
#}
#try:
#    from .local import *
#except ImportError:
#    pass

ALLOWED_HOSTS = ['nw-backend.onrender.com', 'shoshin.world']

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Add WhiteNoise middleware
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True