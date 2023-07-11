from streamlit_elements.core.frame import new_element


class CustomTable:
    
    def MetricTable(self, columns, rows, pre_rows = None, **props):
        if not pre_rows:
            pre_rows = rows
        
        for col in columns:
            col["editable"] = False

        assert len(rows) == len(pre_rows), f"rows and pre_rows must have the same length: {len(rows)} != {len(pre_rows)}"
        return new_element("customTable", "MetricTable")(columns=columns, rows=rows, pre_rows=pre_rows, **props)

