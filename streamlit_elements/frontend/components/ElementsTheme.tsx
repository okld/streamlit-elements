import { useEffect, useState } from "react"
import { PaletteMode } from "@mui/material"
import { Theme as MuiTheme, ThemeProvider, createTheme } from "@mui/material/styles"

const defaultTheme = createTheme()

const ElementsTheme = ({ children, theme }: ElementsThemeProps) => {
  const [elementsTheme, setElementsTheme] = useState<MuiTheme>(createTheme())

  useEffect(() => {
    if (theme !== undefined) {
      const palette = defaultTheme.palette

      setElementsTheme(createTheme({
        palette: {
          mode: theme.base as PaletteMode,
          primary: {
            main: theme.primaryColor ?? palette.primary.main,
          },
          secondary: {
            main: theme.primaryColor ?? palette.primary.main,
          },
          background: {
            default: theme.backgroundColor ?? palette.background.default,
            paper: (theme.base === "dark" && theme.secondaryBackgroundColor) || palette.background.paper,
          },
          text: {
            primary: theme.textColor ?? palette.text.primary
          },
        }
      }))
    }
  }, [ // eslint-disable-line react-hooks/exhaustive-deps
    theme?.base,
    theme?.primaryColor,
    theme?.backgroundColor,
    theme?.secondaryBackgroundColor,
    theme?.textColor,
  ])

  return (
    <ThemeProvider theme={elementsTheme}>
      {children}
    </ThemeProvider>
  )
}

export default ElementsTheme
