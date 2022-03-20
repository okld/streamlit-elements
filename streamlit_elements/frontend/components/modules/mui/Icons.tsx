import dynamic from "next/dynamic"
import ElementsLoading from "../../ElementsLoading"

const cachedIcons: ElementsRecord = {}

const loadMuiIcons: ElementsLoader = element => {
  if (cachedIcons.hasOwnProperty(element)) {
    return cachedIcons[element]
  }

  const icon = dynamic(
    () => import("@mui/icons-material").then((module: any) => module[element]),
    { loading: ElementsLoading, ssr: false }
  )

  cachedIcons[element] = icon

  return icon
}

export default loadMuiIcons
