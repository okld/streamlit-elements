from abc import ABC, abstractmethod
from streamlit_elements.core import format
from streamlit_elements.core.context import get_elements_context
from streamlit_elements.core.element import Element


class ElementsModuleBase(ABC):
    __slots__ = "_module"

    def __init__(self, module):
        self._module = module

    def _create_element(self, element):
        return Element(get_elements_context().frame, self._module, element)

    @abstractmethod
    def __getattr__(self, element):
        pass

    @abstractmethod
    def __getitem__(self, element):
        pass


class ElementsModuleDynamic(ElementsModuleBase, ABC):
    __slots__ = "_format_func"

    def __init__(self, module, format_func=format.pascal_case):
        super().__init__(module)
        self._format_func = format_func

    def __getitem__(self, element):
        return self._create_element(self._format_func(element))

    def __getattr__(self, element):
        return self._create_element(self._format_func(element))


class ElementsModuleStatic(ElementsModuleBase, ABC):

    def __getitem__(self, _):
        raise NotImplementedError("This module supports only a fixed set of elements.")

    def __getattr__(self, _):
        raise NotImplementedError("This module supports only a fixed set of elements.")
