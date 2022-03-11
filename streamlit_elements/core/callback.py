import json
import re

from streamlit import session_state
from streamlit.components.v1 import components
from typing import Callable

from streamlit_elements.core import format
from streamlit_elements.core.exceptions import ElementsFrontendError

CALLBACK_KEY = f"_{__name__}.elements_callback_manager"
FORBIDDEN_ARGS_CHAR_RE = re.compile("\W+")


def _patch_register_widget(register_widget):
    def wrapper_register_widget(*args, **kwargs):
        user_key = kwargs.get("user_key", None)
        callbacks = session_state.get(CALLBACK_KEY, None)

        # Check if a callback was registered for that user_key.
        if user_key is not None and callbacks is not None and user_key in callbacks:
            callback_manager = callbacks[user_key]

            # Add callback-specific args for the real register_widget function.
            kwargs["on_change_handler"] = callback_manager.dispatch

        # Call the original function with updated kwargs.
        return register_widget(*args, **kwargs)

    return wrapper_register_widget

# Patch function once.
if not hasattr(components.register_widget, CALLBACK_KEY):
    components.register_widget = _patch_register_widget(components.register_widget)
    setattr(components.register_widget, CALLBACK_KEY, True)


class ElementsCallbackManager:
    __slots__ = ("_callbacks", "_key")

    def __init__(self, key):
        self._callbacks = {}
        self._key = key

        # Initialize callbacks store.
        if CALLBACK_KEY not in session_state:
            session_state[CALLBACK_KEY] = {}

        # Register a callback for a given element_key.
        session_state[CALLBACK_KEY][key] = self

    def register(self, callback):
        if isinstance(callback, Callable):
            callback = ElementsCallback(callback)

        # Callback IDs are composed of the frame's key and their index
        # in the callbacks dictionary. The index is padded make sure
        # every callback ID has the same length. This is used to order
        # for call ordering.
        callback_id = f"{self._key}{len(self._callbacks):08}"
        self._callbacks[callback_id] = callback.function
        callback.serialize(callback_id)

        return callback

    def dispatch(self):
        # Retrieve data and convert it to json.
        data = json.loads(session_state[self._key], object_hook=lambda d: ElementsCallbackData(d))

        if "error" in data:
            raise ElementsFrontendError(f"In elements frame '{self._key}': {data.error}")

        # Sort data by key.
        data = {k: v for k, v in sorted(data.items())}

        for callback_id, params in data.items():
            if callback_id in self._callbacks:
                self._callbacks[callback_id](**params)


class ElementsCallback:
    __slots__ = ("_function", "_args", "_lazy", "_serialized")

    def __init__(self, function, args=None, lazy=False):
        self._function = function
        self._lazy = lazy
        self._serialized = "()=>{}"
        self._args = args if args is not None else function.__code__.co_varnames
        self._args = (FORBIDDEN_ARGS_CHAR_RE.sub("", key) for key in self._args)

    @property
    def function(self):
        return self._function

    def serialize(self, callback_id):
        args = ",".join(self._args)
        data = f"{format.json(callback_id)}:{{{args}}}"

        if self._lazy:
            # When widget changes, store data in state.
            self._serialized = f"({args})=>{{window.lazyData={{...window.lazyData,{data}}}}}"
        else:
            # When widget changes, send data and state values to Streamlit.
            # Then clear state.
            self._serialized = f"({args})=>send({{{data}}})"

    def __repr__(self):
        return self._serialized


class ElementsCallbackData(dict):

    def __getattr__(self, value):
        return self.__getitem__(value)
