"""
WSGI config for bb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bb.settings.dev")
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))

application = get_wsgi_application()
