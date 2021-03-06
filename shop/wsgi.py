"""
WSGI config for shop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)
application.add_files('/path/to/more/static/files', prefix='more-files/')


application = get_wsgi_application()

# import os
# from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bootcamp.settings")
#
# application = get_wsgi_application()
# application = DjangoWhiteNoise(application)

