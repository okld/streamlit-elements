import * as React from 'react';
import Box from '@mui/material/Box';
import { alpha, styled } from '@mui/material/styles';
import { GridColDef, DataGrid, GridCellParams, gridClasses, GridValidRowModel, useGridApiRef } from '@mui/x-data-grid';

const ODD_OPACITY = 0.2;

const StripedDataGrid = styled(DataGrid)(({ theme }) => ({
  [`& .${gridClasses.row}.even`]: {
    backgroundColor: theme.palette.grey[200],
    '&:hover, &.Mui-hovered': {
      backgroundColor: alpha(theme.palette.primary.main, ODD_OPACITY),
      '@media (hover: none)': {
        backgroundColor: 'transparent',
      },
    },
    '&.Mui-selected': {
      backgroundColor: alpha(
        theme.palette.primary.main,
        ODD_OPACITY + theme.palette.action.selectedOpacity,
      ),
      '&:hover, &.Mui-hovered': {
        backgroundColor: alpha(
          theme.palette.primary.main,
          ODD_OPACITY +
            theme.palette.action.selectedOpacity +
            theme.palette.action.hoverOpacity,
        ),
        // Reset on touch devices, it doesn't add specificity
        '@media (hover: none)': {
          backgroundColor: alpha(
            theme.palette.primary.main,
            ODD_OPACITY + theme.palette.action.selectedOpacity,
          ),
        },
      },
    },
  },
}));


const MetricTable = (props: any) => {
  const apiRef = useGridApiRef();
  return (
    <Box
      sx={props.color_map}
    >
      <div style={{ height: props.height, width: props.witdh }}>
        <StripedDataGrid
          rows={props.rows}
          columns={props.columns}
          getRowClassName={(params) =>
            params.indexRelativeToCurrentPage % 2 === 0 ? 'even' : 'odd'
          }
          getCellClassName={(params: GridCellParams) => {
            return 'blue';
          }}
        />
      </div>
    </Box>
  );
}

// rows={props.rows} columns={props.columns}

const elements: ElementsRecord = { MetricTable }
const loadCustomTable: ElementsLoader = element => elements[element]

export default loadCustomTable