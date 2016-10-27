"""
WSGI config for TWLight project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TWLight.settings.production")

application = get_wsgi_application()

try:
    # If whitenoise is available, use it for serving staticfiles.
    # If it's not, don't.
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)
except ImportError:
    pass