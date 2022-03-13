import { useEffect } from "react"
import Mousetrap from "mousetrap"
import "mousetrap/plugins/global-bind/mousetrap-global-bind"

const Hotkey = ({ sequence, callback, bindInputs, overrideDefault }: ElementsEventHotkeysProps) => {
  useEffect(() => {
    const bind = bindInputs ? Mousetrap.bindGlobal : Mousetrap.bind

    bind(sequence, () => {
      callback()

      if (overrideDefault)
        return false
    })

    return () => {
      Mousetrap.unbind(sequence)
    }
  })

  return null
}

const elements: ElementsRecord = { Hotkey }
const loadHotkey: ElementsLoader = element => elements[element]

export default loadHotkey
