"""
WSGI config for fourteen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/sitemayer/projects/django/fourteen')
sys.path.append('/home/sitemayer/projects/django/fourteen/fourteen')

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fourteen.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'fourteen.settings'
import django
django.setup()

# application = get_wsgi_application()
application = django.core.handlers.wsgi.WSGIHandler()
