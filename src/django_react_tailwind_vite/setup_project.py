import os
from .utils import SetUpRootDir, SetUpFrontendDir, SetUpDjangoDir


class SetUpFrontend:
    def __init__(self, django_project_folder: str):
        self.project_root = os.getcwd()
        self.django_project_folder = django_project_folder

    def set_up_frontend_project(self):
        print(f"📦 Setting up {self.django_project_folder} project files ...")
        root_dir = SetUpRootDir(self.project_root)
        root_dir.set_up_root_dir()
        frontend_dir = SetUpFrontendDir(self.project_root)
        frontend_dir.set_up_frontend_dir()
        django_dir = SetUpDjangoDir(self.project_root, self.django_project_folder)
        django_dir.setup_django_dir()

def main():
    django_project_folder = input("Enter the name of your Django project: ")
    frontend = SetUpFrontend(django_project_folder)
    frontend.set_up_frontend_project()
    print("#" * 50)
    print(f"🎉 Your project {django_project_folder} setup completed successfully!")
    print("#" * 50)
    print(
        "Visit https://github.com/AsinineFatuity/django-react-tailwind-vite#post-script-instructions for post script instructions"
    )
