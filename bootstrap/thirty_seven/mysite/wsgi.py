"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# application = get_wsgi_application()

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/sitemayer/projects/django/thirty_seven')
sys.path.append('/home/sitemayer/projects/django/thirty_seven/mysite')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()

application = django.core.handlers.wsgi.WSGIHandler()
