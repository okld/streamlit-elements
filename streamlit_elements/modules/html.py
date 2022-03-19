from streamlit_elements.core.frame import new_element


class HTML:

    def __getattr__(self, element):
        return new_element("html", element)

    def __getitem__(self, element):
        return new_element("html", element)
