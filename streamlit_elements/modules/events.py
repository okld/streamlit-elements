from streamlit_elements.core.module import ElementsModuleStatic

__all__ = ["event"]


class Hotkey(ElementsModuleStatic):

    def __init__(self):
        super().__init__("eventHotkey")

    def __call__(self, sequence, callback, bind_inputs=False, override_default=False):
        self._create_element("Hotkey")(
            sequence=sequence,
            callback=callback,
            bind_inputs=bind_inputs,
            override_default=override_default,
        )


class Interval(ElementsModuleStatic):

    def __init__(self):
        super().__init__("eventInterval")

    def __call__(self, seconds, callback):
        self._create_element("Interval")(seconds=seconds, callback=callback)


class Events:

    def __init__(self):
        self._on_hotkey = Hotkey()
        self._on_interval = Interval()

    @property
    def on_hotkey(self):
        return self._on_hotkey

    @property
    def on_interval(self):
        return self._on_interval


event = Events()
