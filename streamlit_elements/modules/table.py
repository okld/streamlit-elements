from streamlit_elements.core.frame import new_element

class CustomTable:
    
    def MetricTable(self, columns, rows, height=400, width="100%", cell_colors=None, _use_toolbar=True, **props):
        for col in columns:
            col["editable"] = False

        _color_map = {
            '& .red': {
                "color": "#fc2816",
            },
            '& .green': {
                "color": "#2ECC71",
            },
            '& .blue': {
                "color": "#0000ff",
            },
        }
        if not cell_colors:
            _cell_colors = {}
        else:
            _cell_colors = dict()
            for item in cell_colors:
                _cell_colors.setdefault(item['column'], {})

                if 'id' not in item:
                    # select all rows
                    _cell_colors[item['column']] = item['color']
                elif isinstance(_cell_colors[item['column']], dict):
                    _cell_colors[item['column']].update({
                        item['id']: item['color']
                    })
        return new_element("customTable", "MetricTable")(
            columns=columns,
            rows=rows,
            height=height,
            width=width,
            cell_colors=_cell_colors,
            _color_map=_color_map,
            _use_toolbar=_use_toolbar,
            **props)

