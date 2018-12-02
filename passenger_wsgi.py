import os, sys

site_user_root_dir = '/home/c/catoffnet/swing.tech/public_html'

#project directory
sys.path.append(os.path.join(site_user_root_dir, 'test_project'))
sys.path.append(os.path.join(site_user_root_dir, 'myproject/lib/python2.7/site-packages'))

#project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

#start server
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()