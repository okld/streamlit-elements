from streamlit_elements.core.module import ElementsModuleStatic

__all__ = ["media"]


class Player(ElementsModuleStatic):

    def __init__(self):
        super().__init__("mediaPlayer")

    def __call__(self, url, **props):
        self._create_element("Player")(url=url, **props)


class Media:

    def __init__(self):
        self._player = Player()

    @property
    def player(self):
        return self._player


media = Media()
