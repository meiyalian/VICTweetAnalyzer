<template>
  <div class="Echarts" style="width: 100%;height:100%;">
    <div id="TwitterAPI_Pie" style="width: 100%;height:100%;"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";

export default {
  name: "TwitterPie",
  methods:{
    myEcharts(){
      var chartDom = document.getElementById('TwitterAPI_Pie');
      var myChart = echarts.init(chartDom);
      var option;

      var data = genData(this.twitterAPI);

      option = {
        title: {
          text: '同名数量统计',
          subtext: '纯属虚构',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },

        legend: {
          type: 'scroll',
          orient: 'vertical',
          right: 10,
          top: 20,
          bottom: 20,
          data: data.legendData,

          selected: data.selected
        },
        series: [
          {
            name: 'Local government area',
            type: 'pie',
            radius: '70%',
            center: ['50%', '50%'],
            data: data.seriesData,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };

      function genData(twitterAPI) {
        var legendData = [];
        var seriesData = [];
        for (var obj in twitterAPI){
          legendData.push(twitterAPI[obj].ABB_NAME);
          seriesData.push({
            name: twitterAPI[obj].ABB_NAME,
            value: twitterAPI[obj].sentiment_score
          })
        }
        return {
          legendData: legendData,
          seriesData: seriesData
        };
      }
      option && myChart.setOption(option);
    },
  },
  mounted() {
    this.axios
      .get('http://localhost:80/static/twitterAPI.json')
      .then(response => (
        this.twitterAPI = response.data.LGA,
          // console.log(this.twitterAPI),
          this.myEcharts()
      ));

  }
}
</script>

<style scoped>

</style>
