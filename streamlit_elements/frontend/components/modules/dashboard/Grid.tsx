import React from "react"
import { Global } from "@emotion/react"
import { Responsive, WidthProvider } from "react-grid-layout"
import "react-grid-layout/css/styles.css"
import "react-resizable/css/styles.css"

const ResponsiveGridLayout = WidthProvider(Responsive)
const GridPlaceholderStyle = <Global styles={{
  ".react-grid-item.react-grid-placeholder": {
    background: "transparent !important",
    border: "thin dashed grey !important",
    opacity: ".9 !important",
  }
}}/>

const Grid = ({ children, ...props }: ElementsDashboardGridProps) => (
  <>
    {GridPlaceholderStyle}
    <ResponsiveGridLayout {...props}>
      {[children].flat().map(child => {
        if (React.isValidElement(child) && child.key !== undefined) {
          let style: any = {}
          // @ts-ignore
          if (child.props.hasOwnProperty("style")) {
            // @ts-ignore
            style = child.props.style
          }

          style["height"] = "100%"
          style["width"] = "100%"
          style["boxSizing"] = "border-box"

          // @ts-ignore
          const new_node = React.cloneElement(child, {style: style})
          return (
            <div key={child.key}>
              {new_node}
            </div>
          )
        }
        else {
          return child
        }
      })}
    </ResponsiveGridLayout>
  </>
)

const elements: ElementsRecord = { Grid }
const loadGrid: ElementsLoader = element => elements[element]

export default loadGrid
