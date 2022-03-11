from streamlit_elements.core.module import ElementsModuleStatic

__all__ = ["monaco"]


class Monaco(ElementsModuleStatic):
    """Monaco editor (https://github.com/react-monaco-editor/react-monaco-editor)"""

    def __init__(self):
        super().__init__("editorMonaco")

    def editor(self, **props):
        self._create_element("Editor")(**props)

    def diff(self, **props):
        self._create_element("Diff")(**props)


monaco = Monaco()
