from streamlit_elements.core.module import ElementsModuleDynamic

__all__ = ["mui"]


class MUIIcons(ElementsModuleDynamic):
    """MUI Icons (https://mui.com/components/material-icons)"""

    def __init__(self):
        super().__init__("muiIcons")


class MUILab(ElementsModuleDynamic):
    """MUI Lab (https://mui.com)"""

    def __init__(self):
        super().__init__("muiLab")


class MUIElements(ElementsModuleDynamic):
    """MUI Elements (https://mui.com)"""

    __slots__ = ("_icon", "_lab")

    def __init__(self):
        super().__init__("muiElements")
        self._icon = MUIIcons()
        self._lab = MUILab()

    @property
    def icon(self):
        return self._icon

    @property
    def lab(self):
        return self._lab


mui = MUIElements()
