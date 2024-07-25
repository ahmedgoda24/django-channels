"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from whitenoise import WhiteNoise

from project.settings import BASE_DIR



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django_application = get_asgi_application()
django_application = WhiteNoise(django_application, root=os.path.join(BASE_DIR, 'staticfiles'))
from . import urls # noqa isort:skip
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(urls.websocket_urlpatterns)
    }
)
