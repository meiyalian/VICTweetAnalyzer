<template>
  <div class="pop" style="width: 320px;height: 320px">
    <div class="Echarts" style="width: 100%;height:100%;">
      <div id="Map_Pie" style="width: 100%;height:100%;"></div>
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
          this.myEcharts()
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
          text: this.ABB_NAME,
          subtext: 'Sentiment Score',
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
            radius: ['25%', '50%'],
            center: ['50%', '40%'],
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

</style>
