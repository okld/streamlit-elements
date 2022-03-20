import dynamic from "next/dynamic"
import ElementsLoading from "../../ElementsLoading"

const elements: ElementsRecord = {
  Player: dynamic(() => import("react-player/lazy"), { loading: ElementsLoading, ssr: false }),
}

const loadPlayer: ElementsLoader = element => elements[element]

export default loadPlayer
