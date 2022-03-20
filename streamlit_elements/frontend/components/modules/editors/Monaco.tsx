import dynamic from "next/dynamic"
import { loader } from "@monaco-editor/react"
import ElementsLoading from "../../ElementsLoading"

// Configure a packaged monaco editor to avoid downloading it from CDN.
loader.config({
  paths: {
    vs: "./monaco/vs"
  }
})

const elements: ElementsRecord = {
  Editor: dynamic(() => import("@monaco-editor/react"), { loading: ElementsLoading, ssr: false }),
  Diff: dynamic(() => import("@monaco-editor/react").then(m => m.DiffEditor), { loading: ElementsLoading, ssr: false }),
}

const loadMonaco: ElementsLoader = element => elements[element]

export default loadMonaco
