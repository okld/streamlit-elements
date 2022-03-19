from streamlit_elements.core.frame import new_element


class MUIIcons:
    """MUI Icons (https://mui.com/components/material-icons)"""

    def __getattr__(self, element):
        return new_element("muiIcons", element)

    def __getitem__(self, element):
        return new_element("muiIcons", element)


class MUILab:
    """MUI Lab (https://mui.com)"""

    def __getattr__(self, element):
        return new_element("muiLab", element)

    def __getitem__(self, element):
        return new_element("muiLab", element)


class MUI:
    """MUI Elements (https://mui.com)"""

    __slots__ = ("_icon", "_lab")

    def __init__(self):
        self._icon = MUIIcons()
        self._lab = MUILab()

    @property
    def icon(self):
        return self._icon

    @property
    def lab(self):
        return self._lab

    def __getattr__(self, element):
        return new_element("muiElements", element)

    def __getitem__(self, element):
        return new_element("muiElements", element)
