✨ Streamlit Elements
=====================

[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]

Create a draggable and resizable dashboard in Streamlit, featuring Material UI widgets, Monaco editor (Visual Studio Code), Nivo charts, and more!

Demo
----

[![Open in Streamlit][share_badge]][share_link]

[![Preview][share_video]][share_link]

[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://share.streamlit.io/okld/streamlit-gallery/main?p=elements
[share_video]: https://github.com/okld/streamlit-elements/raw/main/demo.gif

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/okld/streamlit-elements

[pypi_badge]: https://badgen.net/pypi/v/streamlit-elements?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/streamlit-elements


Getting started
---------------

### 1. Introduction

#### Installation

```sh
pip install streamlit-elements
```

#### Available elements and objects

Here is a list of elements and objects you can import in your app:

Element   | Description
:--------:|:-----------
elements  | Create a frame where elements will be displayed.
dashboard | Build a draggable and resizable dashboard.
mui       | Material UI (MUI) widgets and icons.
html      | HTML objects.
monaco    | Monaco code and diff editor that powers Visual Studio Code.
nivo      | Nivo chart library.
media     | Media player.
sync      | Callback to synchronize Streamlit's session state with elements' events data.
lazy      | Defer a callback call until another non-lazy callback is called.

#### Caution

- A few Material UI widgets may not work as expected (ie. modal dialogs and snackbars).
- Using many element frames can significantly impact your app's performance. Try to gather elements in few frames at most.

---

### 2. Display elements

#### 2.1. Create an element with a child

```python
# First, import the elements you need

from streamlit_elements import elements, mui, html

# Elements can't display outside of this frame.
# Native Streamlit widgets will NOT display inside this frame.
#
# elements() takes a key as parameter.
# This key can't be reused by another frame or Streamlit widget.

with elements("new_element"):

    # In this example, "Hello world" is a children of typography.
    #
    # Equivalent React JSX code:
    #
    # <Typography>
    #   Hello world
    # </Typography>

    mui.typography("Hello world")
```
- MUI Typography: https://mui.com/components/typography/

---

#### 2.2. Create an element with multiple children

```python
with elements("multiple_children"):

    # You have access to Material UI icons using: mui.icon.icon_name_here
    # Icons must be written in snake_case, not in camelCase nor in PascalCase.
    #
    # Multiple children can be added in a single element.
    #
    # <Button>
    #   <EmojiPeople />
    #   <DoubleArrow />
    #   Hello world
    # </Button>

    mui.button(
        mui.icon.emoji_people,
        mui.icon.double_arrow,
        "Button with multiple children"
    )

    # You can also add children to an element using the 'with' syntax.
    #
    # <Button>
    #   <EmojiPeople />
    #   <DoubleArrow />
    #   <Typography>
    #     Hello world
    #   </Typography>
    # </Button>

    with mui.button:
        mui.icon.emoji_people()
        mui.icon.double_arrow()
        mui.typography("Button with multiple children")
```
- MUI button: https://mui.com/components/buttons/
- MUI icons: https://mui.com/components/material-icons/

---

#### 2.3. Create an element with nested children

```python
with elements("nested_children"):

    # You can nest children using 'with'.
    #
    # <Paper>
    #   <Typography>
    #     <p>Hello world</p>
    #     <p>Goodbye world</p>
    #   </Typography>
    # </Paper>

    with mui.paper:
        with mui.typography:
            html.p("Hello world")
            html.p("Goodbye world")
```
- MUI paper: https://mui.com/components/paper/

---

#### 2.4. Add properties to an element

```python
with elements("properties"):

    # You can add properties to elements with named parameters.
    # Properties must be written in snake_case, not in camelCase nor in PascalCase.
    #
    # <Paper elevation={3} variant="outlined" square>
    #   <TextField label="My text input" defaultValue="Type here" variant="outlined" />
    # </Paper>

    with mui.paper(elevation=3, variant="outlined", square=True):
        mui.text_field(
            label="My text input",
            default_value="Type here",
            variant="outlined",
        )

    # If you must pass a parameter which is also a Python keyword, use a dictionary
    # to avoid a syntax error.
    #
    # <Collapse in />

    mui.collapse(**{"in": True})

    # Syntax error: 'in' is a Python keyword:
    # mui.collapse(in=True)
```
- MUI text field: https://mui.com/components/text-fields/

---

#### 2.5. Apply custom CSS styles

##### 2.5.1. Material UI elements

```python
with elements("style_mui_sx")

    # For Material UI elements, use the 'sx' property.
    #
    # <Box
    #   sx={{
    #     bgcolor: 'background.paper',
    #     boxShadow: 1,
    #     borderRadius: 2,
    #     p: 2,
    #     minWidth: 300,
    #   }}
    # >
    #   Some text in a styled box
    # </Box>

    mui.box(
        "Some text in a styled box",
        sx={
            "bgcolor": "background.paper",
            "boxShadow": 1,
            "borderRadius": 2,
            "p": 2,
            "minWidth": 300,
        }
    )
```
- MUI's **sx** property: https://mui.com/system/the-sx-prop/

##### 2.5.2. Other elements

```python
with elements("style_elements_css"):

    # For any other element, use the 'css' property.
    #
    # <div
    #   css={{
    #     backgroundColor: 'hotpink',
    #     '&:hover': {
    #         color: 'lightgreen'
    #     }
    #   }}
    # >
    #   This has a hotpink background
    # </div>

    html.div(
        "This has a hotpink background",
        css={
            "backgroundColor": "hotpink",
            "&:hover": {
                "color": "lightgreen"
            }
        }
    )
```
- Emotion's **css** property: https://emotion.sh/docs/css-prop#object-styles

---

### 3. Callbacks

#### 3.1. Retrieve an element's data

```python
with elements("callbacks_retrieve_data"):

    # Some element allows executing a callback on specific event.
    #
    # const [name, setName] = React.useState("")
    # const handleChange = (event) => {
    #   // You can see here that a text field value
    #   // is stored in event.target.value
    #   setName(event.target.value)
    # }
    #
    # <TextField
    #   label="Input some text here"
    #   onChange={handleChange}
    # />

    # Initialize a new item in session state called "text"
    if "my_text" not in st.session_state:
        st.session_state.my_text = ""

    # When our text field changes, this function will be called.
    # To know which parameters are passed to the callback,
    # you can refer to the element's documentation.
    def handle_change(event):
        st.session_state.my_text = event.target.value

    # Here we display what we have typed in our text field
    mui.typography(st.session_state.my_text)

    # And here we give our 'handle_change' callback to the 'on_change'
    # property of the text field.
    mui.text_field(label="Input some text here", on_change=handle_change)
```
- MUI text field event: https://mui.com/components/text-fields/#uncontrolled-vs-controlled
- MUI text field API: https://mui.com/api/text-field/

---

#### 3.2. Synchronize a session state item with an element event using sync()

```python
with elements("callbacks_sync"):

    # If you just want to store callback parameters into Streamlit's session state
    # like above, you can also use the special callback function sync().
    #
    # When an on_change event occurs, the callback is called with an event data object
    # as argument. In the example below, we are synchronizing that event data object with
    # the session state item 'my_event'.
    #
    # If an event passes more than one parameter, you can synchronize as many session state item
    # as needed like so:
    # >>> sync("my_first_param", "my_second_param")
    #
    # If you want to ignore the first parameter of an event but keep synchronizing the second,
    # pass None to sync:
    # >>> sync(None, "second_parameter_to_keep")

    from streamlit_elements import sync

    if "my_event" not in st.session_state:
        st.session_state.my_event = None

    if st.session_state.my_event is not None:
        text = st.session_state.my_event.target.value
    else:
        text = ""

    mui.typography(text)
    mui.text_field(label="Input some text here", on_change=sync("my_event"))
```

---

#### 3.3. Avoid too many reloads with lazy()

```python
with elements("callbacks_lazy"):

    # With the two first examples, each time you input a letter into the text field,
    # the callback is invoked but the whole app is reloaded as well.
    #
    # To avoid reloading the whole app on every input, you can wrap your callback with
    # lazy(). This will defer the callback invocation until another non-lazy callback
    # is invoked. This can be useful to implement forms.

    from streamlit_elements import lazy

    if "first_name" not in st.session_state:
        st.session_state.first_name = None
        st.session_state.last_name = None

    if st.session_state.first_name is not None:
        first_name = st.session_state.first_name.target.value
    else:
        first_name = "John"

    if st.session_state.last_name is not None:
        last_name = st.session_state.last_name.target.value
    else:
        last_name = "Doe"

    def set_last_name(event):
        st.session_state.last_name = event

    # Display first name and last name
    mui.typography("Your first name: ", first_name)
    mui.typography("Your last name: ", last_name)

    # Lazily synchronize on_change with first_name and last_name state.
    # Inputting some text won't synchronize the value yet.
    mui.text_field(label="First name", on_change=lazy(sync("first_name")))

    # You can also pass regular python functions to lazy().
    mui.text_field(label="Last name", on_change=lazy(set_last_name))

    # Here we give a non-lazy callback to on_click using sync().
    # We are not interested in getting on_click event data object,
    # so we call sync() with no argument.
    #
    # You can use either sync() or a regular python function.
    # As long as the callback is not wrapped with lazy(), its invocation will
    # also trigger every other defered callbacks.
    mui.button("Update first namd and last name", on_click=sync())
```

---

#### 3.4. Invoke a callback when a sequence is pressed using event.on_hotkey()

```python
with elements("callbacks_hotkey"):

    # Invoke a callback when a specific hotkey sequence is pressed.
    #
    # For more information regarding sequences syntax and supported keys,
    # go to Mousetrap's project page linked below.
    #
    # /!\ Hotkeys work if you don't have focus on Streamlit Elements's frame /!\
    # /!\ As with other callbacks, this reruns the whole app /!\

    from streamlit_elements import event

    def hotkey_pressed():
        print("Hotkey pressed")

    event.on_hotkey("g", hotkey_pressed)

    # If you want your hotkey to work even in text fields, set bind_inputs to True.
    event.on_hotkey("h", hotkey_pressed, bind_inputs=True)
    mui.text_field(label="Try pressing 'h' while typing some text here.")

    # If you want to override default hotkeys (ie. ctrl+f to search in page),
    # set override_default to True.
    event.on_hotkey("ctrl+f", hotkey_pressed, override_default=True)
```
- Mousetrap: https://craig.is/killing/mice
- Github page: https://github.com/ccampbell/mousetrap

---

#### 3.5. Invoke a callback periodically using event.on_interval()

```python
with elements("callbacks_interval"):

    # Invoke a callback every n seconds.
    #
    # /!\ As with other callbacks, this reruns the whole app /!\

    def call_every_second():
        print("Hello world")

    event.on_interval(1, call_every_second)
```

---

### 4. Draggable and resizable dashboard

```python
with elements("dashboard"):

    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.

    from streamlit_elements import dashboard

    # First, build a default layout for every element you want to include in your dashboard
    #
    # /!\ Properties must be written in snake_case, not in camelCase nor in PascalCase /!\

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.item("first_item", 0, 0, 2, 2),
        dashboard.item("second_item", 2, 0, 2, 2, is_draggable=False, moved=False),
        dashboard.item("third_item", 0, 2, 1, 1, is_resizable=False),
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find here:
    #
    # /!\ Properties must be written in snake_case, not in camelCase nor in PascalCase /!\

    with dashboard(layout):
        mui.paper("First item", key="first_item")
        mui.paper("Second item (cannot drag)", key="second_item")
        mui.paper("Third item (cannot resize)", key="third_item")

    # If you want to retrieve updated layout values after user interactions,
    # you can pass a callback to the on_layout_change event.

    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard() if you want to restore a saved layout.
        print(updated_layout)

    with dashboard(layout, on_layout_change=handle_layout_change):
        mui.paper("First item", key="first_item")
        mui.paper("Second item (cannot drag)", key="second_item")
        mui.paper("Third item (cannot resize)", key="third_item")
```
- Dashboard item properties: https://github.com/react-grid-layout/react-grid-layout#grid-item-props
- Dashboard grid properties (Streamlit Elements uses the Responsive grid layout):
  - https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
  - https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

---

### 5. Other third-party elements

#### 5.1. Monaco code and diff editor

```python
with elements("monaco_editors"):

    # Streamlit Elements embeds Monaco code and diff editor that powers Visual Studio Code.
    # You can configure editor's behavior and features with the 'options' parameter.
    #
    # Elements uses an unofficial React implementation.

    from streamlit_elements import monaco

    if "content" not in st.session_state:
        st.session_state.content = "Default value"

    mui.typography("Content: ", st.session_state.content)

    def update_content(value):
        st.session_state.content = value

    monaco.editor(
        height=300,
        default_value=st.session_state.content,
        on_change=lazy(update_content)
    )

    mui.button("Update content", on_click=sync())

    monaco.diff(
        original="Happy Streamlit-ing!",
        modified="Happy Streamlit-in' with Elements!",
        height=300,
    )
```
- Monaco examples and properties: https://github.com/suren-atoyan/monaco-react
- Code editor options: https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html
- Diff editor options:  https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneDiffEditorConstructionOptions.html
- Monaco project page:  https://microsoft.github.io/monaco-editor/

---

#### 5.2. Nivo charts

```python
with elements("nivo_charts"):

    # Streamlit Elements includes 45 dataviz components powered by Nivo.

    from streamlit_elements import nivo

    DATA = [
        { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
        { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
        { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
        { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
        { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
    ]

    with mui.box(sx={"height": 500}):
        nivo.radar(
            data=DATA,
            keys=[ "chardonay", "carmenere", "syrah" ],
            index_by="taste",
            value_format=">-.2f",
            margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
            border_color={ "from": "color" },
            grid_label_offset=36,
            dot_size=10,
            dot_color={ "theme": "background" },
            dot_border_width=2,
            motion_config="wobbly",
            legends=[
                {
                    "anchor": "top-left",
                    "direction": "column",
                    "translateX": -50,
                    "translateY": -40,
                    "itemWidth": 80,
                    "itemHeight": 20,
                    "itemTextColor": "#999",
                    "symbolSize": 12,
                    "symbolShape": "circle",
                    "effects": [
                        {
                            "on": "hover",
                            "style": {
                                "itemTextColor": "#000"
                            }
                        }
                    ]
                }
            ],
            theme={
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        )
```
- Nivo charts: https://nivo.rocks/
- Github page: https://github.com/plouc/nivo

---

#### 5.3. Media player

```python
with elements("media_player"):

    # Play video from many third-party sources: YouTube, Facebook, Twitch,
    # SoundCloud, Streamable, Vimeo, Wistia, Mixcloud, DailyMotion and Kaltura.
    #
    # Element powered by ReactPlayer.

    from streamlit_elements import media

    media.player(url="https://www.youtube.com/watch?v=iik25wqIuFo", controls=True)
```
- ReactPlayer properties: https://github.com/cookpete/react-player#props
