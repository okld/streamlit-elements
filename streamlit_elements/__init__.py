from streamlit_elements.core.context import get_elements_context as _get_elements_context
from streamlit_elements.core.exceptions import *
from streamlit_elements.modules.callbacks import *
from streamlit_elements.modules.charts import *
from streamlit_elements.modules.dom import *
from streamlit_elements.modules.editors import *
from streamlit_elements.modules.events import *
from streamlit_elements.modules.dashboard import *
from streamlit_elements.modules.media import *
from streamlit_elements.modules.mui import *
from streamlit_elements.version import __version__


def elements(key: str) -> None:
    """Create a Streamlit Elements frame."""
    return _get_elements_context().new_frame(key)
