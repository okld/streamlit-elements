import json


class Element:
    __slots__ = ("_frame", "_module", "_element", "_props", "_children")

    def __init__(self, frame, module, element):
        self._frame = frame
        self._module = json.dumps(module)
        self._element = json.dumps(element)
        self._props = ""
        self._children = ""

    def __enter__(self):
        self._frame.capture_children()

    def __exit__(self, *_):
        self._frame.save_children(self)

    def __call__(self, *children, **props):
        self._frame.register_element(self)

        # Serialize and stringify props and children.
        # Leading underscores in prop keys are stripped to allow passing props
        # that are also python keywords:
        #
        # >>> mui.collapse(in=True)   # Syntax error: 'in' is a python keyword
        # >>> mui.collapse(in_=True)  # Works. React equivalent: <Collapse in={true} />
        self._props += ",".join(
            json.dumps(key.rstrip("_")) + ":" + self._frame.serialize(value)
            for key, value in props.items()
        )
        self._children += ",".join(
            self._frame.serialize(child)
            for child in children
        )

        return self

    def __repr__(self):
        return f"render({self._module},{self._element},{{{self._props}}},[{self._children}])"
