import os
import content
from constants import names


class SetUpDjangoUrlsFile:
    def __init__(self, project_root: str, django_project_folder: str):
        self.PROJECT_ROOT = project_root
        self.URLS_FILE = os.path.join(django_project_folder, names.DJANGO_URLS_FILE)

    def setup_django_urls_file(self):
        print("📦 Setting up Django urls.py file ...")
        with open(self.URLS_FILE, "w") as urls_file:
            urls_file.write(content.DJANGO_URLS_CONTENT)
        print("✅ Django urls.py file created successfully")
