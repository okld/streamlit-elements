from streamlit_elements.core.module import ElementsModuleDynamic

__all__ = ["nivo"]


class Nivo(ElementsModuleDynamic):
    """Nivo charts (https://nivo.rocks)"""

    def __init__(self):
        super().__init__("chartNivo")


nivo = Nivo()
