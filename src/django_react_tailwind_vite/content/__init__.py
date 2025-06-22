from content.package_json import PACKAGE_JSON_CONTENT
from content.vite_config import VITE_CONFIG_CONTENT
from content.requirements import REQUIREMENTS_CONTENT
from content.dwango.manage import write_manage_py_content
from content.dwango.asgi import write_django_asgi_content
from content.dwango.wsgi import write_django_wsgi_content
from content.dwango.settings import write_django_settings_content
from content.html import HOME_HTML_CONTENT
from content.static_dir import MAIN_CSS_CONTENT
from content.gitinore import GITIGNORE_CONTENT
from content.src_dir import INDEX_TSX_CONTENT, APP_TSX_CONTENT, HOME_PAGE_CONTENT
from content.components import (
    COMPONENTS_INDEX_TSX_CONTENT,
    LOADING_INDICATOR_TSX_CONTENT,
    FEEDBACK_TOAST_TSX_CONTENT,
)
from content.environments import DEV_ENV_CONTENT, DEV_PROD_CONTENT
from content.helpers_dir import INTERFACES_FILE_CONTENT, UTILS_FILE_CONTENT
from content.redux_actions import (
    ACTION_TYPES_CONTENT,
    FEEDBACK_TOAST_ACTION_CONTENT,
    LOADING_INDICATOR_ACTION_CONTENT,
    ACTIONS_INDEX_TS_CONTENT,
)
from content.redux_middleware import MIDDLEWARE_INDEX_CONTENT
from content.redux_reducer import (
    LOADING_INDICATOR_REDUCER_CONTENT,
    FEEDBACK_TOAST_REDUCER_CONTENT,
    REDUCER_INDEX_CONTENT,
)
from content.redux_store import REDUX_STORE_CONTENT
from content.hooks import HOOKS_INDEX_TS_CONTENT
from content.ts_config import TS_CONFIG_JSON_CONTENT
from content.dwango.urls import DJANGO_URLS_CONTENT
