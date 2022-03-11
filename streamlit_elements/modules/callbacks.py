import re

from streamlit import session_state
from streamlit_elements.core.callback import ElementsCallback

__all__ = ["sync"]


def sync(*session_state_keys, lazy=False):
    return ElementsCallback(session_state.update, args=session_state_keys, lazy=lazy)
