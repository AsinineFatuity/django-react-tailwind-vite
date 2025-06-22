import os
import content
from constants import names


class SetUpFrontendDir:

    def __init__(self, project_root: str):
        self.PROJECT_ROOT = project_root
        self.FRONTEND_DIR = os.path.join(project_root, names.FRONTEND_DIR)

    def set_up_frontend_dir(self):
        print("📦 Creating frontend folder and initializing files ...")
        os.makedirs(self.FRONTEND_DIR, exist_ok=True)
        os.chdir(self.FRONTEND_DIR)
        with open(names.INDEX_TSX_FILE, "w") as index_ts_file:
            index_ts_file.write(content.INDEX_TSX_CONTENT)
        with open(names.APP_TSX_FILE, "w") as app_tsx_file:
            app_tsx_file.write(content.APP_TSX_CONTENT)
        self._setup_env_dir()
        self._setup_src_dir()
        self._setup_helpers_dir()
        self._setup_hooks_dir()
        self._setup_redux_dir()
        self._setup_components_dir()
        print("✅ Folder frontend set up successfully")
        os.chdir(self.PROJECT_ROOT)

    def _setup_env_dir(self):
        print("📦 Setting up environments folder ...")
        os.makedirs(names.ENVIRONMENTS_DIR, exist_ok=True)
        os.chdir(names.ENVIRONMENTS_DIR)
        with open(names.DEV_ENV_FILE, "w") as dev_env_file:
            dev_env_file.write(content.DEV_ENV_CONTENT)
        with open(names.DEV_PROD_FILE, "w") as prod_env_file:
            prod_env_file.write(content.DEV_PROD_CONTENT)
        print("✅ Folder environments created successfully")
        os.chdir(self.FRONTEND_DIR)

    def _setup_helpers_dir(self):
        print("📦 Setting up helpers folder ...")
        os.makedirs(names.HELPERS_DIR, exist_ok=True)
        os.chdir(names.HELPERS_DIR)
        os.makedirs(names.INTERFACES_DIR, exist_ok=True)
        os.chdir(names.INTERFACES_DIR)
        with open(names.INDEX_TS_FILE, "w") as index_ts_file:
            index_ts_file.write(content.INTERFACES_FILE_CONTENT)
        os.chdir("..")
        os.makedirs(names.UTILS_DIR, exist_ok=True)
        with open(names.INDEX_TS_FILE, "w") as utils_file:
            utils_file.write(content.UTILS_FILE_CONTENT)
        print("✅  Helpers folder created successfully")
        os.chdir("..")

    def _setup_redux_dir(self):
        print("📦 Setting up redux folder ...")
        os.makedirs(names.REDUX_DIR, exist_ok=True)
        os.chdir(names.REDUX_DIR)
        # actions
        os.makedirs(names.ACTIONS_DIR, exist_ok=True)
        os.chdir(names.ACTIONS_DIR)
        with open(names.INDEX_TS_FILE, "w") as index_ts_file:
            index_ts_file.write(content.ACTIONS_INDEX_TS_CONTENT)
        with open(
            names.LOADING_INDICATOR_REDUX_FILE, "w"
        ) as loading_indicator_action_file:
            loading_indicator_action_file.write(
                content.LOADING_INDICATOR_ACTION_CONTENT
            )
        with open(names.FEEDBACK_TOAST_REDUX_FILE, "w") as feedback_toast_action_file:
            feedback_toast_action_file.write(content.FEEDBACK_TOAST_ACTION_CONTENT)
        with open(names.ACTION_TYPES_TS_FILE, "w") as action_types_file:
            action_types_file.write(content.ACTION_TYPES_CONTENT)
        os.chdir("..")
        # middleware
        os.makedirs(names.MIDDLEWARE_DIR, exist_ok=True)
        os.chdir(names.MIDDLEWARE_DIR)
        with open(names.INDEX_TS_FILE, "w") as index_ts_file:
            index_ts_file.write(content.MIDDLEWARE_INDEX_CONTENT)
        os.chdir("..")
        # reducers
        os.makedirs(names.REDUCERS_DIR, exist_ok=True)
        os.chdir(names.REDUCERS_DIR)
        with open(names.INDEX_TS_FILE, "w") as index_ts_file:
            index_ts_file.write(content.REDUCER_INDEX_CONTENT)
        with open(
            names.LOADING_INDICATOR_REDUX_FILE, "w"
        ) as loading_indicator_reducer_file:
            loading_indicator_reducer_file.write(
                content.LOADING_INDICATOR_REDUCER_CONTENT
            )
        with open(names.FEEDBACK_TOAST_REDUX_FILE, "w") as feedback_toast_reducer_file:
            feedback_toast_reducer_file.write(content.FEEDBACK_TOAST_REDUCER_CONTENT)
        os.chdir("..")
        # store
        with open(names.STORE_TS_FILE, "w") as store_ts_file:
            store_ts_file.write(content.REDUX_STORE_CONTENT)
        print("✅ Folder redux created successfully")
        os.chdir("..")

    def _setup_hooks_dir(self):
        print("📦 Setting up hooks folder ...")
        os.makedirs(names.HOOKS_DIR, exist_ok=True)
        os.chdir(names.HOOKS_DIR)
        with open(names.INDEX_TS_FILE, "w") as index_ts_file:
            index_ts_file.write(content.HOOKS_INDEX_TS_CONTENT)
        print("✅ Folder hooks created successfully")
        os.chdir("..")

    def _setup_components_dir(self):
        print("📦 Setting up components folder ...")
        os.makedirs(names.COMPONENTS_DIR, exist_ok=True)
        os.chdir(names.COMPONENTS_DIR)
        with open(names.INDEX_TS_FILE, "w") as index_ts_file:
            index_ts_file.write(content.COMPONENTS_INDEX_TSX_CONTENT)
        with open(names.LOADING_INDICATOR_TSX_FILE, "w") as loading_indicator_tsx_file:
            loading_indicator_tsx_file.write(content.LOADING_INDICATOR_TSX_CONTENT)
        with open(names.FEEDBACK_TOAST_TSX_FILE, "w") as feedback_toast_tsx_file:
            feedback_toast_tsx_file.write(content.FEEDBACK_TOAST_TSX_CONTENT)
        print("✅ Folder components created successfully")
        os.chdir("..")

    def _setup_src_dir(self):
        print("📦 Setting up src folder ...")
        os.makedirs(names.SRC_DIR, exist_ok=True)
        os.chdir(names.SRC_DIR)
        os.makedirs(names.PAGES_DIR, exist_ok=True)
        os.chdir(names.PAGES_DIR)
        with open(names.HOME_TSX_FILE, "w") as home_tsx_file:
            home_tsx_file.write(content.HOME_PAGE_CONTENT)
        print("✅ Folder src created successfully")
        os.chdir("..")
