"""
WSGI config for piter_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import site

site.addsitedir('/var/www/programerblog/lib/python2.7/site-packages')

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/programerblog/bin/piter_site')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "piter_site.settings")

application = get_wsgi_application()
