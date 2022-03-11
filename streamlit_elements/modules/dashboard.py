from streamlit_elements.core.module import ElementsModuleStatic

__all__ = ["dashboard"]


class Dashboard(ElementsModuleStatic):

    def __init__(self):
        super().__init__("dashboard")

    def __call__(self, layout, **grid_props):
        return self._create_element("Dashboard")(layouts={"lg": layout}, **grid_props)

    def item(self, key, x, y, w, h, **item_props):
        return {"i": key, "x": x, "y": y, "w": w, "h": h, **item_props}


dashboard = Dashboard()
