import dynamic from "next/dynamic"
import ElementsLoading from "../../ElementsLoading"

const loadMuiIcons: ElementsLoader = element =>
    dynamic(
        () => import("@mui/icons-material").then((module: any) => module[element]),
        { loading: ElementsLoading, ssr: false }
    )

export default loadMuiIcons
