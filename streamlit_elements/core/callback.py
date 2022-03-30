import inspect
import json
import re

from streamlit import session_state
from streamlit.components.v1 import components
from typing import Callable

from streamlit_elements.core.exceptions import ElementsFrontendError

CALLBACK_KEY = f"{__name__}.elements_callback_manager"
FORBIDDEN_PARAM_CHAR_RE = re.compile("\W+")


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
        self._callbacks[callback_id] = callback.callback
        callback.serialize(callback_id)

        return callback

    def dispatch(self):
        # Retrieve data and convert it to json.
        frontend_data = json.loads(session_state[self._key], object_hook=lambda d: ElementsCallbackData(d))

        if "error" in frontend_data:
            raise ElementsFrontendError(f"In elements frame '{self._key}': {frontend_data.error}")

        # Sort data by key to make sure callbacks are called in order.
        frontend_data = {k: v for k, v in sorted(frontend_data.items())}

        for callback_id, frontend_params in frontend_data.items():
            if callback_id in self._callbacks:
                callback = self._callbacks[callback_id]

                # If callback expect a parameter not defined in params, pass None by default.
                # This will be the case for any param name that starts with an underscore.
                undefined_params = (
                    param
                    for param in _get_parameters(callback)
                    if param not in frontend_params.keys()
                )

                for param in undefined_params:
                    frontend_params[param] = None

                callback(**frontend_params)


class ElementsCallback:
    __slots__ = ("_callback", "_serialized", "_lazy", "_params")

    def __init__(self, callback, params=None):
        self._callback = callback
        self._serialized = "()=>{}"
        self._lazy = False

        if params is not None:
            self._params = params
        else:
            # If no params specified, get them from callback's signature
            self._params = _get_parameters(callback)

        # Make sure params don't contain forbidden characters.
        self._params = tuple(FORBIDDEN_PARAM_CHAR_RE.sub("", key) for key in self._params)

    @property
    def callback(self):
        return self._callback

    def lazy(self):
        self._lazy = True

    def serialize(self, callback_id):
        params = ",".join(self._params)
        data = f"{json.dumps(callback_id)}:{{{params}}}"

        if self._lazy:
            # When widget changes, store data in state.
            self._serialized = f"({params})=>{{window.lazyData={{...window.lazyData,{data}}};}}"
        else:
            # When widget changes, send data and lazy data to Streamlit.
            # Lazy data is cleared once sent.
            self._serialized = f"({params})=>{{send({{...window.lazyData,{data}}});window.lazyData={{}};}}"

    def __repr__(self):
        return self._serialized


class ElementsCallbackData(dict):
    __slots__ = ()

    def __getattr__(self, value):
        return self.__getitem__(value)


def _get_parameters(function):
    return (
        name
        for name, parameter in inspect.signature(function).parameters.items()
        if parameter.kind == parameter.POSITIONAL_OR_KEYWORD
    )
