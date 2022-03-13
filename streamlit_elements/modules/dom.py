from streamlit_elements.core import format
from streamlit_elements.core.module import ElementsModuleDynamic

__all__ = ["html"]


class HTML(ElementsModuleDynamic):

    def __init__(self):
        super().__init__("domHTML", format.lower_case_no_underscore)


html = HTML()
