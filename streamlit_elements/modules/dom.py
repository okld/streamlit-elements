from streamlit_elements.core import format
from streamlit_elements.core.module import ElementsModuleDynamic

__all__ = ["html", "svg"]


class HTML(ElementsModuleDynamic):

    def __init__(self):
        super().__init__("domHTML", format.lower_case)


class SVG(ElementsModuleDynamic):

    def __init__(self):
        super().__init__("domSVG", format.camel_case)


html = HTML()
svg = SVG()
