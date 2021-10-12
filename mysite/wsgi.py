"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

os.environ["SECRET_KEY"] = 'f)(jnv!o&2hxoyw5wv%y1t^tqv52(63hcv8b@$k2e)$@dc^d1m'

application = get_wsgi_application()
