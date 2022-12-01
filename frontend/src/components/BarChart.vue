<template>
  <div id="Candlestick_Chart">
    <el-card style="min-height: 200px; max-height: 800px">
      <div slot="header">Crypto Currency Market Cap(in billions)</div>
      <div>
        <div id="bar_chart" style="width: 450px; height: 300px"></div>
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
import map_data from "../assets/world.json";
import cryptoOwner from "../assets/crypto_owners.json";
export default {
  name: "BarChart",
  data() {
    return {
      map_data: null,
      crypto_owner: cryptoOwner,
    };
  },
  methods: {
    get_map_data(v) {
      // this.$http.post('apis/get_history_data',
      // v
      // )
      // .then(response => {
      // this.history_data = response.data.history_data;
      // console.log(response)
      // console.log(this.history_data);
      this.myEcharts();
      console.log(this.map_data);
      console.log("dsfsd");
      this.myEcharts();

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
      var chartDom = document.getElementById("bar_chart");
      var myChart = this.$echarts.init(chartDom, null, {
        width: 450,
        height: 300,
      });
      var option;


      option = {
        xAxis: {
          type: "category",
          data: ["BTC", "ETH", "USDT", "BNB", "USDC", "BUSD", "XRP", "DOGE", "ADA", "MATIC", "Others"],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: [323.00, 153.00, 65.00, 48.00, 43.00, 22.00, 20.00, 13.00, 10.00, 7.00, 185.00],
            type: "bar",
          },
        ],
      };
      option && myChart.setOption(option);
    },
  },
  mounted() {
    this.myEcharts();
    setTimeout(() => {
      this.get_map_data();
    }, 100);
  },
};
</script>

<style scoped>
</style>
