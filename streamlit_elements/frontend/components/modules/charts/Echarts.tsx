import * as echarts from 'echarts';
import React, { useEffect, useState, useRef } from "react"
import useComponentSize from '@rehooks/component-size'

const BasicCharts = (props: any) => {
  const chartDiv = useRef<HTMLDivElement>(null);
  const size = useComponentSize(chartDiv);
  let chartInstance: echarts.ECharts | null = null;

  function renderChart() {
    if (chartDiv == null){return;}
    //@ts-ignore
    const renderInstance = echarts.getInstanceByDom(chartDiv.current);

    if (renderInstance) {
      chartInstance = renderInstance;
    } else {
      //@ts-ignore
      chartInstance = echarts.init(chartDiv.current);
    }
    chartInstance.setOption(props.options);
  }
  useEffect(() => {
    renderChart();
    if (chartInstance != null) {
      chartInstance.resize({
        width: size.width,
        height: size.height
      });
    }
  }, [chartDiv.current, props.option, size, chartInstance, renderChart]);

  return <div style={{ height: "100%", width: "100%" }} ref={chartDiv}></div>
}


const elements: ElementsRecord = { BasicCharts }
const loadEcharts: ElementsLoader = element => elements[element]

export default loadEcharts