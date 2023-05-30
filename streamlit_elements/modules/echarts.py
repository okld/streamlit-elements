from streamlit_elements.core.frame import new_element


class Echarts:

    def BasicCharts(self, options, height=400, **props):
        return new_element("echarts", "BasicCharts")(options=options, height=height, **props)
