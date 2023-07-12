from streamlit_elements.core.frame import new_element


class CustomTable:
    
    def MetricTable(self, columns, rows, color_map=None, height=400, width="100%", **props):
        for col in columns:
            col["editable"] = False

        if not color_map:
            color_map = {
                '& .red': {
                    "color": "#ff0000",
                },
                '& .green': {
                    "color": "#00ff00",
                },
                '& .blue': {
                    "color": "#0000ff",
                },
            }
        return new_element("customTable", "MetricTable")(columns=columns, rows=rows, color_map=color_map, height=height, width=width, **props)

