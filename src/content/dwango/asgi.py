DJANGO_ASGI_CONTENT = """
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', {}.settings)

application = get_asgi_application()
"""

def write_django_asgi_content(project_name: str):
    asgi_content = DJANGO_ASGI_CONTENT.format(project_name)
    return asgi_content
    
