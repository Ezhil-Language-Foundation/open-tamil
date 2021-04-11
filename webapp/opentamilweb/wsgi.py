# -*- coding: utf-8 -*-
"""
WSGI config for opentamilweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import sys

sys.path.insert(0, '/var/www/tamilpesu_us/')

import os
from django.core.wsgi import get_wsgi_application
import opentamilapp
import opentamilweb

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opentamilweb.settings")

application = get_wsgi_application()
