import json
from contextlib import contextmanager
from streamlit import session_state
from typing import Callable, Iterable, Mapping

from streamlit_elements.core.exceptions import ElementsFrameError
from streamlit_elements.core.callback import ElementsCallbackManager, ElementsCallback
from streamlit_elements.core.element import Element
from streamlit_elements.core.render import render_component

ELEMENTS_FRAME_KEY = f"_{__name__}.elements_frame"


def get_elements_frame():
    if ELEMENTS_FRAME_KEY not in session_state:
        raise ElementsFrameError("Frame was not created.")

    return session_state[ELEMENTS_FRAME_KEY]


@contextmanager
def new_frame(key):
    if ELEMENTS_FRAME_KEY in session_state:
        # Ignore this frame.
        yield
        return

    frame = ElementsFrame(key)
    session_state[ELEMENTS_FRAME_KEY] = frame

    try:
        yield
        javascript = repr(frame)

        if javascript:
            render_component(js=javascript, key=key, default="{}")

    finally:
        del session_state[ELEMENTS_FRAME_KEY]


def new_element(module, element):
    if ELEMENTS_FRAME_KEY not in session_state:
        raise ElementsFrameError("Cannot create element outside a frame.")

    return Element(session_state[ELEMENTS_FRAME_KEY], module, element)


class ElementsFrame:
    __slots__ = ("_callback_manager", "_children", "_parents", "_key")

    def __init__(self, key):
        self._callback_manager = ElementsCallbackManager(key)
        self._children = {}
        self._parents = []
        self._key = key

    def register_element(self, element):
        if element not in self._children:
            self._children[element] = False

    def ignore_element(self, element):
        if element in self._children:
            self._children[element] = True

    def capture_children(self):
        self._parents.append(self._children)
        self._children = {}

    def save_children(self, element):
        children = self._children
        self._children = self._parents.pop()

        element(*(child for child, ignored in children.items() if not ignored))

    def serialize(self, obj):
        if isinstance(obj, Element):
            self.ignore_element(obj)
            return repr(obj)

        elif isinstance(obj, (Callable, ElementsCallback)):
            callback = self._callback_manager.register(obj)
            return repr(callback)

        elif isinstance(obj, Mapping):
            items = (json.dumps(key) + ":" + self.serialize(value) for key, value in obj.items())
            items = ",".join(items)
            return f"{{{items}}}"

        elif isinstance(obj, Iterable) and not isinstance(obj, str):
            items = (self.serialize(item) for item in obj)
            items = ",".join(items)
            return f"[{items}]"

        else:
            return json.dumps(obj)

    def __repr__(self):
        return self.serialize(child for child, ignored in self._children.items() if not ignored)
