import os
from django.core.wsgi import get_wsgi_application

# Tell Django where your settings are
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_tennis_club.settings')

# This is the "app" instance the server uses
application = get_wsgi_application()
