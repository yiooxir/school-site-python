import os
import sys

path = '/var/www/school-nn'
if path not in sys.path:
    sys.path.insert(0, '/var/www')

sys.path.insert(0,os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]))

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
