import os
import sys
sys.path.append('/home/apixserver/public_html/APIXServer/APIXServer')
sys.path.append('/home/apixserver/public_html/APIXServer/env/lib/python2.7/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'APIXServer.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
