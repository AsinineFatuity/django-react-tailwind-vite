DJANGO_URLS_CONTENT = """
from django.contrib import admin
from django.urls import path, re_path

from django.http import HttpRequest
from django.views.generic import TemplateView
from django.conf import settings


class HomeView(TemplateView):
    env_template_dict = {
        settings.DEBUG: "home.html",
        not settings.DEBUG: "index.html",
    }
    template_name = env_template_dict[settings.DEBUG]
    context = {}

    def get(self, request: HttpRequest, *args, **kwargs):
        self.context = {}
        return self.render_to_response(self.context)

    def post(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response(self.context)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    re_path(r"^app/.*$", HomeView.as_view(), name="app")
]
"""
