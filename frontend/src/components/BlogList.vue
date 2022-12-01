<template>
  <div id="Candlestick_Chart">
    <el-card style="min-height: 200px; max-height: 800px">
      <div slot="header">Crypto Owner Map</div>
      <div>
        <div id="owner_map" style="width: 400px; height: 300px"></div>
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
  name: "BlogList",
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
      // console.log(this.map_data);
      // console.log("dsfsd");
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
      var chartDom = document.getElementById("owner_map");
      var myChart = this.$echarts.init(chartDom, null, {
        width: 400,
        height: 300,
      });
      var option;
      myChart.hideLoading();
      echarts.registerMap("Owner_Map", map_data, {
        Alaska: {
          left: -131,
          top: 25,
          width: 15,
        },
        Hawaii: {
          left: -110,
          top: 28,
          width: 5,
        },
        "Puerto Rico": {
          left: -76,
          top: 26,
          width: 2,
        },
      });

      var option = {
        // title: {
        //   text: "Crypto Owner Map (2022)",
        //   subtext: "Data from www.census.gov",
        //   sublink: "http://www.census.gov/popest/data/datasets.html",
        //   left: "right",
        // },
        tooltip: {
          trigger: "item",
          showDelay: 0,
          transitionDuration: 0.2,
        },
        visualMap: {
          left: "right",
          min: 500000,
          max: 38000000,
          inRange: {
            color: [
              "#313695",
              "#4575b4",
              "#74add1",
              "#abd9e9",
              "#e0f3f8",
              "#ffffbf",
              "#fee090",
              "#fdae61",
              "#f46d43",
              "#d73027",
              "#a50026",
            ],
          },
          text: ["High", "Low"],
          // calculable: true,
        },
        toolbox: {
          show: true,
          //orient: 'vertical',
          left: "left",
          top: "top",
          feature: {
            dataView: { readOnly: false },
            restore: {},
            saveAsImage: {},
          },
        },
        series: [
          {
            name: "Number of Crypto Owners",
            type: "map",
            roam: true,
            map: "Owner_Map",
            emphasis: {
              label: {
                show: true,
              },
            },
            data: this.crypto_owner,
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
