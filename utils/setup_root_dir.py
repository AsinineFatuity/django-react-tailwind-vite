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
        self._setup_webpack_config_files()
        self._setup_templates_folder()
        self._set_up_static_folder()

    def _setup_package_json_file(self):
        print("📦 Setting up package.json file and installing dependencies ...")
        with open(names.PACKAGE_JSON_FILE, "w") as package_json_file:
            package_json_file.write(content.PACKAGE_JSON_CONTENT)
        print("✅ package.json file created successfully")
        print("📦 Updating dependencies ...")
        subprocess.run(["npx", "npm-check-updates", "-u"])
        print("✅ Dependencies upgraded successfully")

    def _setup_webpack_config_files(self):
        print("📦 Setting up webpack configuration files ...")
        os.makedirs(names.WEBPACK_DIR, exist_ok=True)
        os.chdir(names.WEBPACK_DIR)
        with open(names.WEBPACK_COMMON_CONFIG_FILE, "w") as webpack_common_file:
            webpack_common_file.write(content.WEBPACK_COMMON_CONTENT)
        print("✅ webpack.common.js file created successfully")
        with open(names.WEBPACK_DEV_CONFIG_FILE, "w") as webpack_dev_file:
            webpack_dev_file.write(content.WEBPACK_DEV_CONTENT)
        print("✅ webpack.dev.js file created successfully")
        with open(names.WEBPACK_PROD_CONFIG_FILE, "w") as webpack_prod_file:
            webpack_prod_file.write(content.WEBPACK_PROD_CONTENT)
        print("✅ webpack.prod.js file created successfully")
        print("✅ Webpack configuration files created successfully")
        os.chdir(self.PROJECT_ROOT)

    def _setup_templates_folder(self):
        print("📦 Setting up templates folder ...")
        os.makedirs(names.TEMPLATES_DIR, exist_ok=True)
        os.chdir(names.TEMPLATES_DIR)
        with open(names.INDEX_HTML_FILE, "w") as index_html_file:
            index_html_file.write(content.INDEX_HTML_CONTENT)
        print("✅ index.html file created successfully")
        with open(names.HOME_HTML_FILE, "w") as home_html_file:
            home_html_file.write(content.HOME_HTML_CONTENT)
        print("✅ home.html file created successfully")
        print("✅ Templates folder created successfully")
        os.chdir(self.PROJECT_ROOT)

    def _set_up_static_folder(self):
        print("📦 Setting up static folder ...")
        os.makedirs(names.STATIC_DIR, exist_ok=True)
        os.chdir(names.STATIC_DIR)
        with open(names.INDEX_BUNDLE_JS_FILE, "w") as index_bundle_js_file:
            index_bundle_js_file.write("")
        print("✅ Static folder created successfully")
        os.chdir(self.PROJECT_ROOT)

    def _setup_tsconfig_file(self):
        print("📦 Setting up tsconfig.json file ...")
        with open(names.TS_CONFIG_FILE, "w") as ts_config_file:
            ts_config_file.write(content.TS_CONFIG_JSON_CONTENT)
        print("✅ tsconfig.json file created successfully")
        os.chdir(self.PROJECT_ROOT)
