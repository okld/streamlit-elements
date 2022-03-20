from streamlit_elements.core.frame import new_element


class Editors:

    def Monaco(self, **props):
        """Monaco editor (https://github.com/react-monaco-editor/react-monaco-editor)"""
        new_element("editorMonaco", "Editor")(**props)

    def MonacoDiff(self, **props):
        """Monaco editor (https://github.com/react-monaco-editor/react-monaco-editor)"""
        new_element("editorMonaco", "Diff")(**props)
