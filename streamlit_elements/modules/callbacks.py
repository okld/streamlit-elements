from functools import partial
from streamlit import session_state
from streamlit_elements.core.callback import ElementsCallback
from typing import Callable, List, Union


def sync(*session_state_keys: List[str]):
    # Replace None keys with an underscore.
    session_state_keys = (key if key is not None else "_" for key in session_state_keys)

    return ElementsCallback(session_state.update, params=session_state_keys)


def lazy(callback: Union[Callable, ElementsCallback]):
    if isinstance(callback, Callable):
        callback = ElementsCallback(callback, params=None)

    callback.lazy()

    return callback
