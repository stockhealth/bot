# faq_project/asgi.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faq_project.settings')

application = get_asgi_application()
