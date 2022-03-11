Streamlit Elements
==================

[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]

Streamlit Elements brings many react components to Streamlit, with a few lines of code.


Features
--------

- Material UI widgets (including lab and icons).
- Draggable and resizable dashboard layout.
- Callbacks support.
- Monaco editor (the code editor that powers Visual Studio Code).
- Nivo charts.
- React player.
- HTML and SVG tags.
- Hotkey and interval events support.

Getting started
---------------

### Installation

```sh
pip install streamlit-elements
```

### Usage

```python
import streamlit as st

from streamlit_elements import (
    # This is used to create a frame where elements will be displayed.
    elements,

    # Elements
    mui,        # Material UI widgets and icons
    dashboard,  # Draggable and resizable grid layout
    monaco,     # Monaco code editor (editor, diff)
    nivo,       # Nivo charts
    html,       # HTML tags
    svg,        # SVG tags
    player,     # React player

    # Events (on_hotkey, on_interval)
    event,

    # Callback
    sync,
)

# This creates a new IFrame to display elements.
#
# /!\ Native Streamlit widgets WON'T render inside.
#
with elements("props_and_children"):

    # Create a new Material UI typography element.
    # https://mui.com/components/typography/
    #
    # "Hello world" is a children of typography.
    # Equivalent React code:
    #
    # <Typography>
    #   Hello world
    # </Typography>
    #
    mui.typography("Hello world")

    # Create a new button with multiple children and icons.
    # https://mui.com/components/buttons/
    # https://mui.com/components/material-icons/
    #
    # You have access to Material UI icons using 'mui.icon.icon_name_here'
    # Icons must be written in snake_case, not in camelCase nor PascalCase.
    #
    # Multiple children can be added in a single element.
    #
    # <Button>
    #   <EmojiPeople />
    #   <DoubleArrow />
    #   Hello world
    # </Button>
    #
    mui.button(
        mui.icon.emoji_people,
        mui.icon.double_arrow,
        "Hello world"
    )

    # Create a new Material UI paper element with nested children.
    # https://mui.com/components/paper/
    #
    # You can also add children to an element using the 'with' syntax.
    #
    # <Paper>
    #   <Typography>
    #     <p>Hello world</p>
    #     <p>Goodbye world</p>
    #   </Typography>
    # </Paper>
    #
    with mui.paper:
        with mui.typography:
            html.p("Hello world")
            html.p("Goodbye world")

    # Create a text field inside a paper element.
    # https://mui.com/components/text-fields/
    #
    # You can add properties to elements with named parameters.
    # Like icons, elements and properties must be written in snake_case,
    # not in camelCase nor PascalCase (ie. TextField -> text_field).
    #
    # If you must pass a parameter that happens to be a Python keyword, use
    # the following syntax:
    #
    # >>> mui.collapse(in=True)         # Syntax error: 'in' is a Python keyword.
    # >>> mui.collapse(**{"in": True})  # Works.
    #
    # <Paper elevation={3} variant="outlined" square>
    #   <TextField label="My text input" defaultValue="Type here" variant="outlined" />
    # </Paper>
    #
    with mui.paper(elevation=3, variant="outlined", square=True):
        mui.text_field(label="My text input", default_value="Type here", variant="outlined")

    # Apply custom styles to elements using 'sx' property on Material UI elements,
    # or 'style' on other elements.
    # https://mui.com/system/the-sx-prop/
    #
    # Style dictionary keys are written in camelCase, not in snake_case nor PascalCase (ie. fontWeight).
    #
    mui.box("Style changed with sx!", sx={"color": "text.primary", "fontSize": 34, "fontWeight": "medium"})
    html.div("Style chnaged with style!", style={"color": "blue", "fontSize": 34, "fontWeight": "medium"})

with elements("callback_examples"):
    pass

with elements("dashboard_examples"):
    pass

with elements("events_examples"):
    pass
```


Demo
----

[![Open in Streamlit][share_badge]][share_link]

[![Preview][share_img]][share_link]

[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://share.streamlit.io/okld/streamlit-gallery/main?p=elements
[share_img]: https://raw.githubusercontent.com/okld/streamlit-elements/main/preview.png

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/okld/streamlit-elements

[pypi_badge]: https://badgen.net/pypi/v/streamlit-elements?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/streamlit-elements
