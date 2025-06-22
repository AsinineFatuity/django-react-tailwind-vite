DJANGO_WSGI_CONTENT = """
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{}.settings')

application = get_wsgi_application()
"""

def write_django_wsgi_content(project_name: str):
    asgi_content = DJANGO_WSGI_CONTENT.format(project_name)
    return asgi_content