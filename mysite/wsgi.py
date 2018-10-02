"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD
=======
# from whitenoise.django import DjangoWhiteNoise
>>>>>>> 10bef286ea21e1a42225756e8cac5a3192f294fd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
<<<<<<< HEAD
=======
# application = DjangoWhiteNoise(application)
>>>>>>> 10bef286ea21e1a42225756e8cac5a3192f294fd
