import os
import subprocess
from constants import names
from utils import SetUpRootDir, SetUpFrontendDir, SetUpDjangoUrlsFile


class SetUpFrontend:

    def __init__(self, django_project_folder: str):
        self.project_root = os.getcwd()
        self.django_project_folder = django_project_folder

    def set_up_frontend_project(self):
        if not self._create_django_project_folder():
            return

        root_dir = SetUpRootDir(self.project_root)
        root_dir.set_up_root_dir()
        frontend_dir = SetUpFrontendDir(self.project_root)
        frontend_dir.set_up_frontend_dir()
        django_urls_file = SetUpDjangoUrlsFile(
            self.project_root, self.django_project_folder
        )
        django_urls_file.setup_django_urls_file()
    
    def _create_django_project_folder(self):
        # Create the Django project folder if it does not exist
        if not os.path.exists(self.django_project_folder):
            try:
                subprocess.run(["django-admin", "startproject", self.django_project_folder, "."], check=True)
                print(f"✅ Initialized django project: {self.django_project_folder}")
                return True
            except OSError as e:
                print(f"❌ Failed to initialize Django project: {e}")
        # check django folder is valid
        unique_project_files = [names.DJANGO_ASGI_FILE, names.DJANGO_WSGI_FILE]
        for root, dirs, files in os.walk(self.django_project_folder):
            if any(file in files for file in unique_project_files):
                return True
        print(
            "❌ Django project folder is not valid, please create a django project and try again"
        )
        return False
        


django_project_folder = input("Enter the name of your Django project: ")
frontend = SetUpFrontend(django_project_folder)
frontend.set_up_frontend_project()
print("#" * 50)
print("🎉 Frontend project setup completed successfully!")
print("#" * 50)
print("Visit https://github.com/AsinineFatuity/django-react-bootstrap-webpack#post-script-instructions for post script instruction")