import React from "react"
import { Responsive, WidthProvider } from "react-grid-layout"
import "react-grid-layout/css/styles.css"
import "react-resizable/css/styles.css"

const ResponsiveGridLayout = WidthProvider(Responsive)

const Dashboard = ({ children, ...props }: ElementsDashboardProps) =>
  <ResponsiveGridLayout {...props}>
    {[children].flat().map(child => {
      if (React.isValidElement(child) && child.key !== undefined) {
        if (!child.props.hasOwnProperty("style")) {
          child.props.style = {}
        }

        const style = child.props.style
        style.height = "100%"
        style.width = "100%"
        style.boxSizing = "border-box"

        return <div key={child.key}>{child}</div>
      }
      else {
        return child
      }
    })}
  </ResponsiveGridLayout>

const elements: ElementsRecord = { Dashboard }
const loadDashboard: ElementsLoader = element => elements[element]

export default loadDashboard
