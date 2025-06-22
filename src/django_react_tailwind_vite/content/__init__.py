from .package_json import PACKAGE_JSON_CONTENT
from .vite_config import VITE_CONFIG_CONTENT
from .requirements import REQUIREMENTS_CONTENT
from .dwango import (
    write_manage_py_content,
    write_django_asgi_content,
    write_django_wsgi_content,
    write_django_settings_content,
    DJANGO_URLS_CONTENT
)
from .html import HOME_HTML_CONTENT
from .static_dir import MAIN_CSS_CONTENT
from .gitinore import GITIGNORE_CONTENT
from .src_dir import INDEX_TSX_CONTENT, APP_TSX_CONTENT, HOME_PAGE_CONTENT
from .components import (
    COMPONENTS_INDEX_TSX_CONTENT,
    LOADING_INDICATOR_TSX_CONTENT,
    FEEDBACK_TOAST_TSX_CONTENT,
)
from .environments import DEV_ENV_CONTENT, DEV_PROD_CONTENT
from .helpers_dir import INTERFACES_FILE_CONTENT, UTILS_FILE_CONTENT
from .redux_actions import (
    ACTION_TYPES_CONTENT,
    FEEDBACK_TOAST_ACTION_CONTENT,
    LOADING_INDICATOR_ACTION_CONTENT,
    ACTIONS_INDEX_TS_CONTENT,
)
from .redux_middleware import MIDDLEWARE_INDEX_CONTENT
from .redux_reducer import (
    LOADING_INDICATOR_REDUCER_CONTENT,
    FEEDBACK_TOAST_REDUCER_CONTENT,
    REDUCER_INDEX_CONTENT,
)
from .redux_store import REDUX_STORE_CONTENT
from .hooks import HOOKS_INDEX_TS_CONTENT
from .ts_config import TS_CONFIG_JSON_CONTENT