from streamlit_elements.modules.dashboard import Dashboard
from streamlit_elements.modules.editors import Editors
from streamlit_elements.modules.events import Events
from streamlit_elements.modules.html import HTML
from streamlit_elements.modules.media import Media
from streamlit_elements.modules.mui import MUI
from streamlit_elements.modules.nivo import Nivo
from streamlit_elements.modules.callbacks import sync, lazy

__all__ = ["dashboard", "editor", "event", "html", "media", "mui", "nivo", "sync", "lazy"]


dashboard = Dashboard()
editor = Editors()
event = Events()
html = HTML()
media = Media()
mui = MUI()
nivo = Nivo()
