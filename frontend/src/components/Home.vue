<template>
  <div class="Home" align="center">
    <!--    <div align="right">-->
    <!--      <div style="width: 300px">-->
    <!--        <h1 style="text-align: right">每个人都有属于自己的一片森林，</h1>-->
    <!--        <h1 style="text-align: right">迷失的人迷失了， </h1>-->
    <!--        <h1 style="text-align: right">相逢的人会再相逢。</h1>-->
    <!--      </div>-->
    <!--    </div>-->
    <!--    <div style="width: 300px">-->
    <!--    </div>-->
    <el-row :gutter="10">
      <el-col :span="8">
        <right_pie_echarts></right_pie_echarts>
      </el-col>
      <el-col :span="8">
        <BlogList></BlogList>
      </el-col>

      <el-col :span="8">
        <el-card style="min-height: 200px; max-height: 800px">
        <div slot="header">Model Result</div>
        <img src="../../src/assets/bitcoin_price_prediction.png" height="295px" width="400px"></img>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="10">
      <el-col :span="8">
        <BarChart></BarChart>
      </el-col>
      <el-col :span="8">
        <AddBlog></AddBlog>
      </el-col>
      <el-col :span="8">
      <el-card style="min-height: 200px; max-height: 800px">
      <div slot="header">Model Result</div>
                <img src="../../src/assets/model_loss.png" height="295px" width="400px"></img>
                </el-card>
      </el-col>
    </el-row>

    <!-- <el-row :gutter="10">
      <el-col :span="18"> </el-col>
      <el-col :span="6">
        <p>fsdgsdfgdf</p>
      </el-col>
    </el-row>

    <el-row :gutter="10">
      <el-col :span="18"> </el-col>
      <el-col :span="6">
        <p>fsdgsdfgdf</p>
      </el-col>
    </el-row> -->

    <el-row :gutter="10">
      <el-col :span="24">
        <el-card>
          <ul>
  <li><b>Sentiment: </b>Cryptocurrencies are very volatile and subject to a variety of factors, and due to the recent poor economic conditions, the general perception in the market is negative. </li>
  <li><b>Crypto Owner Map: </b>The worldwide distribution of crypto owners is a crucial statistic for grasping how big the potential for crypto is in different areas. Hence, a interactive choropleth map is integrated into our project for displaying the worldwide distribution of crypto owners.  </li>
  <li><b>Crypto Currency Market Cap: </b>For a cryptocurrency like Bitcoin, market capitalization (or market cap) is the total value of all the coins that have been mined.</li>
  <li><b>Candlestick Chart: </b>A candlestick shows the change in the price of an asset over a period of time. As the basic indicator in a crypto chart, each candlestick represents a specific price movement, including the opening and closing prices, as well as the highest and lowest price points.</li>
  <li><b>Bitcoin price prediction: </b>The result tells a very small gap between the prediction and actual price of bitcoin.</li>
  <li><b>Model loss: </b>With the loss graph, we could see that the training loss and testing loss reached very close to zero towards the end of the validation process.</li>
</ul>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
// import Status from '@/components/Status'
import left_pie_echarts from "@/components/echarts_dic/left_pie_echarts";
import right_pie_echarts from "@/components/echarts_dic/right_pie_echarts";
import BlogList from "@/components/BlogList";
import AddBlog from "@/components/AddBlog";
import BarChart from "@/components/BarChart";

export default {
  name: "Home",
  components: {
    // Status,
    left_pie_echarts,
    right_pie_echarts,
    BlogList,
    AddBlog,
    BarChart,
  },
  data() {
    return {
      playm: false,
      mp3: "",
      audio: "",
      name: "",
    };
  },

  methods: {
    play: function (url, name) {
      console.log(name, url);
      this.audio = url;
      this.name = name;
      this.playm = true;
    },
  },
  created() {
    // this.$http.get('apis/get_info?mp3=yep')
    //   .then(response => {
    //     this.mp3 = response.data
    //   }, error => {
    //     console.log('mp3 error')
    //   })
    // fetch('apis/get_info?mp3=yep', {
    //   method: 'get',
    // })
    //   .then(response => {
    //     return response.json()
    //   })
    //   .then(data => {
    //     this.mp3 = data
    //   })
  },
};
</script>

<style scoped>
.grid_content {
  background: #0b2e13;
  height: auto;
  width: auto;
}
ul,
li {

  display: inline-block;
  text-align: left;
}
</style>
