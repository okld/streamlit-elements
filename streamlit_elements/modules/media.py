from streamlit_elements.core.module import ElementsModuleStatic

__all__ = ["player"]


class Player(ElementsModuleStatic):

    def __init__(self):
        super().__init__("mediaPlayer")

    def __call__(self, url, **props):
        self._create_element("Player")(url=url, **props)


player = Player()
