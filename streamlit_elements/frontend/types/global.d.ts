import { ComponentProps, Theme as StreamlitTheme } from "streamlit-component-lib"

declare global {
  interface Window {
    lazyData: Record<string, any> = {}
  }

  type ElementsAppProps = ComponentProps & {
    args: {
      js: string
    }
  }

  type ElementsResizerProps = {
    children: React.ReactChild | React.ReactChild[]
  }

  type ElementsThemeProps = {
    theme: StreamlitTheme | undefined
    children: React.ReactChild | React.ReactChild[]
  }

  type ElementsDashboardGridProps = {
    props: Record<string, any>
    children: React.ReactChild[]
  }

  type ElementsComponentType = React.ComponentType<any> | string

  type ElementsLoader = (element: string) => ElementsComponentType

  type ElementsRecord = Record<string, ElementsComponentType>

  type ElementsLoaderRecord = Record<string, ElementsLoaderType>

  type ElementsFunctionType = (...args: any[]) => any

  type ElementsEventLoadProps = {
    callback: ElementsFunctionType
  }

  type ElementsEventUpdateProps = {
    code: string
    callback: ElementsFunctionType
  }

  type ElementsEventChangeProps = {
    callback: ElementsFunctionType
  }

  type ElementsEventIntervalProps = {
    seconds: number
    callback: ElementsFunctionType
  }

  type ElementsEventHotkeysProps = {
    sequence: string
    callback: ElementsFunctionType
    bindInputs: boolean
    overrideDefault: boolean
  }
}
