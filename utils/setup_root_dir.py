import os
import subprocess
from constants import names
import content


class SetUpRootDir:

    def __init__(self, project_root: str):
        self.PROJECT_ROOT = project_root

    def set_up_root_dir(self):
        self._setup_package_json_file()
        self._setup_tsconfig_file()
        self._setup_vite_config_files()
        self._setup_templates_folder()
        self._set_up_static_folder()

    def _setup_package_json_file(self):
        print("📦 Setting up package.json file")
        with open(names.PACKAGE_JSON_FILE, "w") as package_json_file:
            package_json_file.write(content.PACKAGE_JSON_CONTENT)
        print("✅ package.json file created successfully")
        
    def _setup_vite_config_files(self):
        with open(names.VITE_CONFIG_FILE, "w") as vite_config_file:
            vite_config_file.write(content.VITE_CONFIG_CONTENT)
        print("✅ Vite configuration files created successfully")
        os.chdir(self.PROJECT_ROOT)

    def _setup_templates_folder(self):
        print("📦 Setting up templates folder ...")
        os.makedirs(names.TEMPLATES_DIR, exist_ok=True)
        os.chdir(names.TEMPLATES_DIR)
        with open(names.HOME_HTML_FILE, "w") as home_html_file:
            home_html_file.write(content.HOME_HTML_CONTENT)
        print("✅ Templates folder created successfully")
        os.chdir(self.PROJECT_ROOT)

    def _set_up_static_folder(self):
        print("📦 Setting up static folder ...")
        os.makedirs(names.STATIC_DIR, exist_ok=True)
        print("✅ Static folder created successfully")
        os.chdir(self.PROJECT_ROOT)

    def _setup_tsconfig_file(self):
        print("📦 Setting up tsconfig.json file ...")
        with open(names.TS_CONFIG_FILE, "w") as ts_config_file:
            ts_config_file.write(content.TS_CONFIG_JSON_CONTENT)
        print("✅ tsconfig.json file created successfully")
        os.chdir(self.PROJECT_ROOT)
