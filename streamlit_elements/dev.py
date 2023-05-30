from streamlit_elements.core.frame import new_frame as _new_frame
from streamlit_elements.core.exceptions import *
from streamlit_elements.modules import *
from streamlit_elements.version import __version__
from streamlit.components.v1 import declare_component
import uuid


render_component = declare_component("streamlit_elements", url="http://localhost:3001")

render_component(js='[render("html","script",{"type":"text/javascript"},["var option = 123123; alert(option)"]),render("html","s",{},["var option = 123123; console.log(option)", "second row"]),render("html","div",{"css":{"backgroundColor":"hotpink","&:hover":{"color":"lightgreen"}}},["This has a hotpink background"])]',
                    key="streamlit_elements.core.frame.elements_frame.echarts_js" + uuid.uuid4().hex, default="{}")


# nivo_str = '[render("muiElements","Box",{"sx":{"height":500}},[render("chartNivo","Line",{"data":[{"id":"japan","color":"hsl(335, 70%, 50%)","data":[{"x":"plane","y":31},{"x":"helicopter","y":215},{"x":"boat","y":270},{"x":"train","y":215},{"x":"subway","y":143},{"x":"bus","y":189},{"x":"car","y":56},{"x":"moto","y":32},{"x":"bicycle","y":113},{"x":"horse","y":291},{"x":"skateboard","y":34},{"x":"others","y":20}]}],"margin":{"top":50,"right":110,"bottom":50,"left":60},"xScale":{"type":"point"},"yScale":{"type":"linear","min":"auto","max":"auto","stacked":true,"reverse":false},"yFormat":">-.2f","axisTop":null,"axisRight":null,"axisBottom":{"tickSize":5,"tickPadding":5,"tickRotation":0,"legend":"transportation","legendOffset":36,"legendPosition":"middle"},"axisLeft":{"tickSize":5,"tickPadding":5,"tickRotation":0,"legend":"count","legendOffset":-40,"legendPosition":"middle"},"pointSize":10,"pointColor":{"theme":"background"},"pointBorderWidth":2,"pointBorderColor":{"from":"serieColor"},"pointLabelYOffset":-12,"useMesh":true,"legends":[{"anchor":"bottom-right","direction":"column","justify":false,"translateX":100,"translateY":0,"itemsSpacing":0,"itemDirection":"left-to-right","itemWidth":80,"itemHeight":20,"itemOpacity":0.75,"symbolSize":12,"symbolShape":"circle","symbolBorderColor":"rgba(0, 0, 0, .5)","effects":[{"on":"hover","style":{"itemBackground":"rgba(0, 0, 0, .03)","itemOpacity":1}}]}]},[])])]'
# render_component(js=nivo_str,
#                     key="streamlit_elements.core.frame.elements_frame.nivo_charts" + uuid.uuid4().hex, default="{}")

echarts_str = '[render("echarts","BasicCharts",{"options":{"xAxis":{"type":"category","data":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]},"yAxis":{"type":"value"},"series":[{"data":[150,230,224,218,135,147,260],"type":"line"}]},"height":1000},[])]'
render_component(js=echarts_str,
                    key="streamlit_elements.core.frame.elements_frame.echarts" + uuid.uuid4().hex, default="{}")
