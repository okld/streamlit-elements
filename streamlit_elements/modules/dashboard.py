from streamlit_elements.core.frame import new_element


class Dashboard:

    def Item(self, i, x, y, w, h, **props):
        return {"i": i, "x": x, "y": y, "w": w, "h": h, **props}

    def Grid(self, layout, **props):
        return new_element("dashboardGrid", "Grid")(layouts={"lg": layout}, **props)
