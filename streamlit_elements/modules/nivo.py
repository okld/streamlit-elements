from streamlit_elements.core.frame import new_element


class Nivo:
    """Nivo charts (https://nivo.rocks)"""

    def __getattr__(self, element):
        return new_element("chartNivo", element)

    def __getitem__(self, element):
        return new_element("chartNivo", element)
