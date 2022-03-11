from contextlib import contextmanager
from streamlit import session_state

from streamlit_elements.core.exceptions import ElementsFrameError
from streamlit_elements.core.frame import ElementsFrame
from streamlit_elements.core.render import render_component

ELEMENTS_CONTEXT_KEY = f"_{__name__}.elements_context"

def get_elements_context():
    if ELEMENTS_CONTEXT_KEY not in session_state:
        session_state[ELEMENTS_CONTEXT_KEY] = ElementsContext()

    return session_state[ELEMENTS_CONTEXT_KEY]


class ElementsContext:
    __slots__ = "_frame"

    def __init__(self):
        self._frame = None

    @property
    def frame(self):
        if self._frame is None:
            raise ElementsFrameError("No Elements Frame created.")
        return self._frame

    @contextmanager
    def new_frame(self, key):
        if self._frame is not None:
            raise ElementsFrameError("Cannot create a frame inside another frame.")

        self._frame = ElementsFrame(key)

        try:
            yield
            javascript = repr(self._frame)

            if javascript:
                render_component(js=javascript, key=key, default="{}")

        finally:
            self._frame = None
