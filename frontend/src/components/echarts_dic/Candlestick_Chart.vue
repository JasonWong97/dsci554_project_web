<template>
  <div id="Candlestick_Chart">
    <el-card style="min-height: 200px; max-height: 400px">
      <div slot="header">Candlestick Chart</div>
      <div>
        <el-select
          v-model="value"
          placeholder="Select"
          @change="get_history_data(value)"
        >
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </div>
      <div>
        <div id="main3" style="width: 450px; height: 400px"></div>
      </div>
    </el-card>
  </div>
</template>

<script>
import * as echarts from "echarts/core";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import { PieChart } from "echarts/charts";
import { CanvasRenderer } from "echarts/renderers";
import btcData from "../../assets/BTC-USD.json";
import ethData from "../../assets/ETH-USD.json";
import usdtData from "../../assets/USDT-USD.json";
import adaData from "../../assets/ADA-USD.json";
import bnbData from "../../assets/BNB-USD.json";
export default {
  name: "Candlestick_Chart",
  data() {
    return {
      options: [
        {
          value: "BTC",
          label: "BTC",
        },
        {
          value: "ETH",
          label: "ETH",
        },
        {
          value: "USDT",
          label: "USDT",
        },
        {
          value: "ADA",
          label: "ADA",
        },
        {
          value: "BNB",
          label: "BNB",
        },
      ],
      value: "BTC",
      history_data: "",
      btc_data: btcData,
      eth_data: ethData,
      usdt_data: usdtData,
      ada_data: adaData,
      bnb_data: bnbData,
    };
  },
  methods: {
    get_history_data(v) {
      // this.$http.post('apis/get_history_data',
      // v
      // )
      // .then(response => {
      // this.history_data = response.data.history_data;
      // console.log(response)
      // console.log(this.history_data);
      // this.myEcharts();
      // console.log(this.btc_data);
      // console.log("dsfsd");
      if (v == "BTC") {
        this.history_data = this.btc_data;
        this.myEcharts();
      } else if (v == "ETH") {
        this.history_data = this.eth_data;
        this.myEcharts();
      } else if (v == "USDT") {
        this.history_data = this.usdt_data;
        this.myEcharts();
      } else if (v == "ADA") {
        this.history_data = this.ada_data;
        this.myEcharts();
      } else if (v == "BNB") {
        this.history_data = this.bnb_data;
        this.myEcharts();
      }

      // })
    },

    myEcharts() {
      echarts.use([
        TitleComponent,
        TooltipComponent,
        LegendComponent,
        PieChart,
        CanvasRenderer,
      ]);
      var chartDom = document.getElementById("main3");
      var myChart = this.$echarts.init(chartDom, null, {
        width: 450,
        height: 400,
      });
      var option;

      var upColor = "#ec0000";
      var upBorderColor = "#8A0000";
      var downColor = "#00da3c";
      var downBorderColor = "#008F28";

      var dataCount = 2e2;
      var data = generateOHLC(this.history_data);
      console.log(data);
      console.log(this.history_data);
      var option = {
        dataset: {
          source: data,
        },
        // title: {
        //   text: 'Data Amount: ' + echarts.format.addCommas(dataCount)
        // },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "line",
          },
        },
        // toolbox: {
        //   feature: {
        //     dataZoom: {
        //       yAxisIndex: false,
        //     },
        //   },
        // },
        grid: [
          {
            left: "10%",
            right: "5%",
            bottom: 200,
          },
          {
            left: "10%",
            right: "10%",
            height: 80,
            bottom: 80,
          },
        ],
        xAxis: [
          {
            type: "category",
            scale: true,
            boundaryGap: false,
            // inverse: true,
            axisLine: { onZero: false },
            splitLine: { show: false },
            splitNumber: 20,
            min: "dataMin",
            max: "dataMax",
          },
          {
            type: "category",
            gridIndex: 1,
            scale: true,
            boundaryGap: false,
            axisLine: { onZero: false },
            axisTick: { show: false },
            splitLine: { show: false },
            axisLabel: { show: false },
            splitNumber: 20,
            min: "dataMin",
            max: "dataMax",
          },
        ],
        yAxis: [
          {
            scale: true,
            splitArea: {
              show: true,
            },
          },
          {
            scale: true,
            gridIndex: 1,
            splitNumber: 2,
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: { show: false },
          },
        ],
        // dataZoom: [
        //   {
        //     type: "inside",
        //     xAxisIndex: [0, 1],
        //     start: 10,
        //     end: 100,
        //   },
        //   {
        //     show: true,
        //     xAxisIndex: [0, 1],
        //     type: "slider",
        //     bottom: 10,
        //     start: 10,
        //     end: 100,
        //   },
        // ],
        visualMap: {
          show: false,
          seriesIndex: 1,
          dimension: 6,
          pieces: [
            {
              value: 1,
              color: upColor,
            },
            {
              value: -1,
              color: downColor,
            },
          ],
        },
        series: [
          {
            type: "candlestick",
            itemStyle: {
              color: upColor,
              color0: downColor,
              borderColor: upBorderColor,
              borderColor0: downBorderColor,
            },
            encode: {
              x: 0,
              y: [1, 4, 3, 2],
            },
          },
          // {
          //   name: "Volumn",
          //   type: "bar",
          //   xAxisIndex: 1,
          //   yAxisIndex: 1,
          //   itemStyle: {
          //     color: "#7fbe9e",
          //   },
          //   large: true,
          //   encode: {
          //     x: 0,
          //     y: 5,
          //   },
          // },
        ],
      };

      function generateOHLC(history_data) {
        var data = [];
        var len = history_data.length;

        for (var i = 0; i < len; i++) {
          // ['open', 'close', 'lowest', 'highest', 'volumn']
          // [1, 4, 3, 2]
          data[i] = [
            history_data[i]["Date"],
            history_data[i]["Open"].toFixed(2), // open
            history_data[i]["High"].toFixed(2), // highest
            history_data[i]["Low"].toFixed(2), // lowest
            history_data[i]["Close"].toFixed(2), // close
            history_data[i]["Volume"].toFixed(0),
            getSign(history_data[i]["Open"], history_data[i]["Close"]), // sign
          ];
          // console.log(data[i]);
        }

        return data;

        function getSign(openVal, closeVal) {
          var sign;
          if (openVal > closeVal) {
            sign = -1;
          } else if (openVal < closeVal) {
            sign = 1;
          } else {
            sign = 1;
          }

          return sign;
        }
      }

      option && myChart.setOption(option);
    },
  },
  mounted() {
    this.myEcharts();
    setTimeout(() => {
      this.get_history_data("BTC");
    }, 100);
  },
};
</script>

<style scoped>
</style>
