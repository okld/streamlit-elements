import dynamic from "next/dynamic"
import ElementsLoading from "../components/ElementsLoading"

const ElementsApp = dynamic(
  () => import("../components/ElementsApp"),
  { loading: ElementsLoading, ssr: false }
)

export default ElementsApp
