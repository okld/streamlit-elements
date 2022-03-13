from streamlit_elements.core import format


class Element:
    __slots__ = ("_frame", "_module", "_element", "_props", "_children")

    def __init__(self, frame, module, element):
        self._frame = frame
        self._module = format.json(module)
        self._element = format.json(element)
        self._props = ""
        self._children = ""

    def __enter__(self):
        self._frame.capture_children()

    def __exit__(self, *_):
        self._frame.save_children(self)

    def __call__(self, *children, **props):
        self._frame.register_element(self)

        # Serialize and stringify props and children.
        self._props += ",".join(
            format.json(format.camel_case(key)) + ":" + self._frame.serialize(value)
            for key, value in props.items()
        )
        self._children += ",".join(
            self._frame.serialize(child)
            for child in children
        )

        return self

    def __repr__(self):
        return f"render({self._module},{self._element},{{{self._props}}},[{self._children}])"
