<template>
  <div class="pop" style="width: 660px;height: 500px">
    <div class="Echarts" style="width: 100%;height:100%;">
      <div id="title">{{this.ABB_NAME}}</div>
      <el-row>
        <el-col :span="12"><div id="Map_Pie" style="width: 100%;height:200px;"></div></el-col>
        <el-col :span="12"><div id="Map_Pie2" style="width: 100%;height:200px;"></div></el-col>
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
          text: 'Sentiment Score',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: '0',
          top: '10%'
        },
        series: [
          {
            name: 'Sentiment Score',
            type: 'pie',
            radius: ['45%', '80%'],
            center: ['50%', '55%'],
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

      option = {
        title: {
          text: 'Sentiment Score',
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
            center: ['50%', '55%'],
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
    myEcharts3(){
      var chartDom = document.getElementById('Map_Pie3');
      var myChart = echarts.init(chartDom);
      var option;
      var ABB_NAME = this.ABB_NAME

      var DATA = this.twitterAPI.filter(function (f) {
        return f.ABB_NAME == ABB_NAME
      })

      option = {
        title: {
          text: 'Sentiment Score',
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
            center: ['50%', '55%'],
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
