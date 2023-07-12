import React, { useEffect, useState, useRef } from "react"
import Box from '@mui/material/Box';
import { alpha, styled } from '@mui/material/styles';
import { DataGrid, GridCellParams, gridClasses } from '@mui/x-data-grid';

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
  return (
    <Box
      sx={props.color_map}
    >
      <div style={{ height: props.height, width: props.width }}>
        <StripedDataGrid
          rows={props.rows}
          columns={props.columns}
          getRowClassName={(params) =>
            params.indexRelativeToCurrentPage % 2 === 0 ? 'even' : 'odd'
          }
          getCellClassName={(params: GridCellParams) => {
            if(props.cell_colors.size === 0){return ''}
            let item = props.cell_colors[params.field]
            if(item === undefined){return ''}

            if(typeof item === "string"){return item}
            if(params.row === undefined){return ''}
            let col_name = params.field
            let item1 = item[params.row[col_name]]
            if(typeof item1 === "string"){return item1}
            return '';
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