<template>
  <div class="pop" style="width: 660px;height: 500px">
    <div class="Echarts" style="width: 100%;height:100%;">
      <div id="title">{{this.ABB_NAME}}</div>
      <el-row>
        <el-col :span="11"><div id="Map_Pie" style="width: 100%;height:200px;"></div></el-col>
        <el-col :span="13"><div id="Map_Pie2" style="width: 100%;height:200px;"></div></el-col>
      </el-row>
      <el-row>
        <el-col :span="24"><div id="Map_Pie3" style="width: 100%;height:300px;"></div></el-col>
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
    }
  },
  mounted() {
    this.axios
      .get('http://localhost:80/static/twitterAPI.json')
      .then(response => (
        this.twitterAPI = response.data.LGA,
          this.myEcharts(),
          this.myEcharts2(),
          this.myEcharts3()
  ));

  },
  methods:{
    myEcharts(){
      var chartDom = document.getElementById('Map_Pie');
      var myChart = echarts.init(chartDom);
      var option;
      var ABB_NAME = this.ABB_NAME

      var DATA = this.twitterAPI.filter(function (f) {
        return f.ABB_NAME == ABB_NAME
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
        return f.ABB_NAME == ABB_NAME
      })

      console.log(DATA[0].age_distribution[0].five_to_nineteen);
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
              {value: DATA[0].age_distribution[0].five_to_nineteen, name: 'Age level: 5-19'},
              {value: DATA[0].age_distribution[0].twenty_to_thirtynine, name: 'Age level: 20-39'},
              {value: DATA[0].age_distribution[0].forty_to_sixty, name: 'Age level: 40-60'},
            ]
          }
        ]
      };
      option && myChart.setOption(option);
    },
    myEcharts3(){
      var chartDom = document.getElementById('Map_Pie3');
      var myChart = echarts.init(chartDom);
      var option;
      var ABB_NAME = this.ABB_NAME

      var DATA = this.twitterAPI.filter(function (f) {
        return f.ABB_NAME == ABB_NAME
      })

      console.log(DATA[0].top_five_emojis);

      option = {
        title: {
          text: 'Top 5 Emoji',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'horizontal',
          x:'center',
          top: '8%'
        },
        series: [
          {
            name: 'Top 5 Emoji',
            type: 'pie',
            radius: ['45%', '80%'],
            center: ['50%', '60%'],
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
              {value: DATA[0].top_five_emojis[0].ratio, name: DATA[0].top_five_emojis[0].code},
              {value: DATA[0].top_five_emojis[1].ratio, name: DATA[0].top_five_emojis[1].code},
              {value: DATA[0].top_five_emojis[2].ratio, name: DATA[0].top_five_emojis[2].code},
              {value: DATA[0].top_five_emojis[3].ratio, name: DATA[0].top_five_emojis[3].code},
              {value: DATA[0].top_five_emojis[4].ratio, name: DATA[0].top_five_emojis[4].code},
            ]
          }
        ]
      };
      option && myChart.setOption(option);
    },

  },

};
</script>

<style scoped>
#title{
  text-align:center;
  font-size: 28px;
  font-weight: bold;
}
</style>
