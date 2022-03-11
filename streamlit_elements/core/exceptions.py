__all__ = [
    "ElementsError",
    "ElementsFrameError",
    "ElementsFrontendError",
]


class ElementsError(Exception):
    """A Streamlit Elements error occured."""


class ElementsFrameError(ElementsError):
    """A frame error occured."""


class ElementsFrontendError(ElementsError):
    """A frontend error occured."""
