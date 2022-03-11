import { useEffect } from "react"

const Interval = ({ seconds, callback }: ElementsEventIntervalProps) => {
  useEffect(() => {
    const interval = setInterval(callback, seconds * 1000)

    return () => {
      clearInterval(interval)
    }
  })

  return null
}

const elements: ElementsRecord = { Interval }
const loadInterval: ElementsLoader = element => elements[element]

export default loadInterval
