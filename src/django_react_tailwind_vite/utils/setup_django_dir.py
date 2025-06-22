import os
from .. import content
from ..constants import names


class SetUpDjangoDir:
    def __init__(self, project_root: str, django_project_folder: str):
        self.PROJECT_ROOT = project_root
        os.makedirs(django_project_folder, exist_ok=True)
        self.django_project_folder = django_project_folder

    def setup_django_dir(self):
        print("📦 Setting up Django project files ...")
        self._setup_django_urls_file()
        self._setup_django_settings_file()
        self._setup_django_asgi_file()
        self._setup_django_wsgi_file()
        os.chdir(self.PROJECT_ROOT)
        with open(names.MANAGE_PY_FILE, "w") as manage_file:
            manage_file.write(
                content.write_manage_py_content(self.django_project_folder)
            )
        print("✅ Django project files created successfully")

    def _setup_django_urls_file(self):
        django_urls_file = os.path.join(
            self.django_project_folder, names.DJANGO_URLS_FILE
        )
        with open(django_urls_file, "w") as urls_file:
            urls_file.write(content.DJANGO_URLS_CONTENT)

    def _setup_django_settings_file(self):
        dj_settings_file = os.path.join(
            self.django_project_folder, names.DJANGO_SETTINGS_FILE
        )
        with open(dj_settings_file, "w") as settings_file:
            settings_file.write(
                content.write_django_settings_content(self.django_project_folder)
            )

    def _setup_django_asgi_file(self):
        dj_asgi_file = os.path.join(self.django_project_folder, names.DJANGO_ASGI_FILE)
        with open(dj_asgi_file, "w") as settings_file:
            settings_file.write(
                content.write_django_asgi_content(self.django_project_folder)
            )

    def _setup_django_wsgi_file(self):
        dj_asgi_file = os.path.join(self.django_project_folder, names.DJANGO_WSGI_FILE)
        with open(dj_asgi_file, "w") as settings_file:
            settings_file.write(
                content.write_django_wsgi_content(self.django_project_folder)
            )

    def _setup_django_init_file(self):
        dj_init_file = os.path.join(self.django_project_folder, names.DJANGO_INIT_FILE)
        with open(dj_init_file, "w") as init_file:
            init_file.write("# Django project initialization file\n")
