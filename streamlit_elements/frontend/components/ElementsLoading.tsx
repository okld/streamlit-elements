import { Skeleton, CircularProgress, Grid } from "@mui/material"

// const ElementsLoading = () =>
//   <Grid container direction="column" alignItems="center">
//     <CircularProgress />
//   </Grid>

const ElementsLoading = () =>
  <Grid container direction="column">
    <Skeleton height={45} width="100%" animation="wave" />
  </Grid>

export default ElementsLoading
