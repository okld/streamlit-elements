from typing import Callable, Iterable, Mapping

from streamlit_elements.core import format
from streamlit_elements.core.callback import ElementsCallbackManager, ElementsCallback
from streamlit_elements.core.element import Element


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
            items = (format.json(key) + ":" + self.serialize(value) for key, value in obj.items())
            items = ",".join(items)
            return f"{{{items}}}"

        elif isinstance(obj, Iterable) and not isinstance(obj, str):
            items = (self.serialize(item) for item in obj)
            items = ",".join(items)
            return f"[{items}]"

        else:
            return format.json(obj)

    def __repr__(self):
        return self.serialize(child for child, ignored in self._children.items() if not ignored)
