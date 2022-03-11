import dynamic from "next/dynamic"
import ElementsLoading from "../../ElementsLoading"

const elements: ElementsRecord = {
    Editor: dynamic(() => import("@monaco-editor/react"), { loading: ElementsLoading, ssr: false }),
    Diff: dynamic(() => import("@monaco-editor/react").then(m => m.DiffEditor), { loading: ElementsLoading, ssr: false }),
}

const loadMonaco: ElementsLoader = element => elements[element]

export default loadMonaco
