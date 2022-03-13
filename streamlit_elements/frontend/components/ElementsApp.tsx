import React, { useEffect, useState } from "react"
import Mousetrap from "mousetrap"
import { ErrorBoundary } from "react-error-boundary"
import { NoSsr } from "@mui/material"
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib"
import { dequal } from "dequal/lite"
import { jsx } from '@emotion/react'

import ElementsResizer from "./ElementsResizer"
import ElementsTheme from "./ElementsTheme"

import loadDashboard from "./modules/dashboard/Dashboard"
import loadHotkey from "./modules/events/Hotkey"
import loadHtml from "./modules/dom/HTML"
import loadInterval from "./modules/events/Interval"
import loadMonaco from "./modules/editors/Monaco"
import loadMuiElements from "./modules/mui/Elements"
import loadMuiIcons from "./modules/mui/Icons"
import loadMuiLab from "./modules/mui/Lab"
import loadNivo from "./modules/charts/Nivo"
import loadPlayer from "./modules/media/Player"

const loaders: ElementsLoaderRecord = {
  // Charts
  chartNivo: loadNivo,

  // Dashboard
  dashboard: loadDashboard,

  // DOM
  domHTML: loadHtml,

  // Events
  eventHotkey: loadHotkey,
  eventInterval: loadInterval,

  // Editor
  editorMonaco: loadMonaco,

  // Media
  mediaPlayer: loadPlayer,

  // MUI
  muiElements: loadMuiElements,
  muiIcons: loadMuiIcons,
  muiLab: loadMuiLab,
}

const getReplacer = () => {
  const seen = new WeakSet()

  return (key: string, value: any) => {
    if (key.startsWith("_") || value instanceof Window) {
      return
    }

    // Check cyclic object values.
    // See: https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Errors/Cyclic_object_value
    if (value instanceof Object && value !== null) {
      if (seen.has(value)) {
        return
      }
      seen.add(value);
    }

    return value;
  };
};

const send = (data: Record<string, any>) => {
  // Add a timestamp to make sure data is unique to force Streamlit to update.
  data = { ...data, timestamp: Date.now() }
  // Send data to Streamlit.
  Streamlit.setComponentValue(JSON.stringify(data, getReplacer()))
}

const render = (module: string, element: string, props: any, children: React.ReactNode[]) => {
  if (!loaders.hasOwnProperty(module)) {
    throw new Error(`Module ${module} does not exist`)
  }

  const loadedElement = loaders[module](element)
  if (loadedElement === undefined) {
    throw new Error(`Element ${element} does not exist in module ${module}`)
  }

  return jsx(loadedElement, props, ...children)
}

const ElementsApp = ({ args, theme }: ElementsAppProps) => {
  const [js, setJs] = useState("return []")

  useEffect(() => {
    setJs(`"use strict";try{return(${args.js});}catch(error){send({error:error.message});return([]);}`)

    // If user presses "r" while focusing Elements IFrame,
    // rerun Streamlit app by sending an empty value.
    Mousetrap.bind("r", () => { send({}) })

    return () => {
      Mousetrap.unbind("r")
    }
  }, [args.js])

  return (
    <ElementsResizer>
      <NoSsr>
        <ElementsTheme theme={theme}>
          <ErrorBoundary fallback={<div/>} onError={error => send({ error: error.message })}>
            {jsx("div", null, ...new Function("render", "send", "window", js)(render, send, window))}
          </ErrorBoundary>
        </ElementsTheme>
      </NoSsr>
    </ElementsResizer>
  )
}

export default withStreamlitConnection(React.memo(ElementsApp, dequal))
