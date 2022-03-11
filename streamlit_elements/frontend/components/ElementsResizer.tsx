import ResizeObserver from "resize-observer-polyfill"
import { Streamlit } from "streamlit-component-lib"

const resizeObserver = new ResizeObserver((entries: any) => {
  Streamlit.setFrameHeight(entries[0].contentRect.height + 25)
})

const observeElement = (element: HTMLDivElement | null) => {
  if (element !== null)
    resizeObserver.observe(element)
  else
    resizeObserver.disconnect()
}

const ElementsResizer = ({ children }: ElementsResizerProps) =>
  <div ref={observeElement}>
    {children}
  </div>

export default ElementsResizer
