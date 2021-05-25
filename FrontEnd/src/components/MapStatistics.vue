<template>
  <div class="pop" style="width: 660px;height: 350px">
    <div class="Echarts" style="width: 100%;height:100%;">
      <div class="title">{{this.ABB_NAME}}</div>
      <el-row>
        <el-col :span="11"><div id="Map_Pie" style="width: 100%;height:200px;"></div></el-col>
        <el-col :span="13"><div id="Map_Pie2" style="width: 100%;height:200px;"></div></el-col>
      </el-row>
      <el-row>
        <el-col :span="24">
          <div style="width: 100%;height:50px;">
            <div class="title">Top 5 Emoji</div>
            <el-row class="emoji">
              <el-col :span="2" style="color: white">a</el-col>
              <el-col :span="4"> {{top_five_emojis[0].emojicode}} </el-col>
              <el-col :span="4"> {{top_five_emojis[1].emojicode}} </el-col>
              <el-col :span="4"> {{top_five_emojis[2].emojicode}} </el-col>
              <el-col :span="4"> {{top_five_emojis[3].emojicode}} </el-col>
              <el-col :span="4"> {{top_five_emojis[4].emojicode}} </el-col>
              <el-col :span="2"></el-col>
            </el-row>

          </div></el-col>
      </el-row>



    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";

export default {
  name: 'MapStatistics',
  props: ['ABB_NAME'],
  data() {
    return {
      top_five_emojis:[
        {"emojicode": '', ",number": null},
        {"emojicode": '', ",number": null},
        {"emojicode": '', ",number": null},
        {"emojicode": '', ",number": null},
        {"emojicode": '', ",number": null},
      ]
    }
  },
  mounted() {
    this.axios
      .get('http://localhost:80/static/twitterAPI_All.json')
      .then(response => (
        this.twitterAPI = response.data.data,
          this.number = this.LGANumber(),
          this.top_five_emojis = response.data.data[this.number].top_five_emojis,
          this.myEcharts(),
          this.myEcharts2()
      ));

  },
  methods:{
    myEcharts(){
      var chartDom = document.getElementById('Map_Pie');
      var myChart = echarts.init(chartDom);
      var option;
      var ABB_NAME = this.ABB_NAME

      var DATA = this.twitterAPI.filter(function (f) {
        return f.area == ABB_NAME
      })

      option = {
        title: {
          text: 'Sentiment Percentage',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: '0',
          top: '14%'
        },
        series: [
          {
            name: 'Sentiment Score',
            type: 'pie',
            radius: ['45%', '80%'],
            center: ['55%', '55%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '14',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              {value: DATA[0].positive, name: 'Positive'},
              {value: DATA[0].negative, name: 'Negative'},
            ]
          }
        ]
      };
      option && myChart.setOption(option);
    },
    myEcharts2(){
      var chartDom = document.getElementById('Map_Pie2');
      var myChart = echarts.init(chartDom);
      var option;
      var ABB_NAME = this.ABB_NAME

      var DATA = this.twitterAPI.filter(function (f) {
        return f.area == ABB_NAME
      })

      // console.log(DATA[0].age_distribution[0].five_to_nineteen);
      // console.log(DATA[0].age_distribution.adults_ratio)
      option = {

        title: {
          text: 'Age Level',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: '0',
          top: '14%'
        },
        series: [
          {
            name: 'Age Level',
            type: 'pie',
            radius: ['60%', '80%'],
            center: ['60%', '55%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '14',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              {value: DATA[0].age_distribution.median_age, name: 'Age level: 5-19'},
              {value: DATA[0].age_distribution.teenagers_and_young_adults_ratio, name: 'Age level: 20-39'},
              {value: DATA[0].age_distribution.adults_ratio, name: 'Age level: 40-60'},
              {value: DATA[0].age_distribution.middle_age_and_above_ratio, name: 'Age level: 40-60'},
            ]
          }
        ]
      };
      option && myChart.setOption(option);
    },
    LGANumber(){
      for (var obj in this.twitterAPI){
        if(this.twitterAPI[obj].area == this.ABB_NAME){
          return obj;
        }
      }
    }
  },

};
</script>

<style scoped>
.title{
  text-align:center;
  font-size: 28px;
  font-weight: bold;
}
.emoji{
  margin-top: 5%;
  font-size: 30px;
}
</style>
