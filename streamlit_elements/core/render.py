from pathlib import Path
from streamlit.components.v1 import declare_component
from streamlit_elements import version

if version.__release__:
    ELEMENT_FRONTEND = {"path": (Path(version.__file__).parent/"frontend/build").resolve()}
else:
    ELEMENT_FRONTEND = {"url": "http://localhost:3001"}

render_component = declare_component("streamlit_elements", **ELEMENT_FRONTEND)
