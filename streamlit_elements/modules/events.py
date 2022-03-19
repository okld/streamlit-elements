from streamlit_elements.core.frame import new_element


class Events:

    def Hotkey(self, sequence, callback, bindInputs=False, overrideDefault=False):
        new_element("eventHotkey", "Hotkey")(
            sequence=sequence,
            callback=callback,
            bindInputs=bindInputs,
            overrideDefault=overrideDefault,
        )

    def Interval(self, seconds, callback):
        new_element("eventInterval", "Interval")(
            seconds=seconds,
            callback=callback
        )
