<template>
  <div class="Echarts" style="width: 100%;height:100%;">
    <div id="twitterTime" style="width: 100%;height:100%;"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";

export default {
  name: "TwitterTime",
  methods:{
    myEcharts2(){
      var chartDom = document.getElementById('twitterTime');
      var myChart = echarts.init(chartDom);
      var option;



      var timeData = ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00',
                      '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',];

      option = {
        title: {
          text: '雨量流量关系图',
          subtext: '数据来自西安兰特水电测控技术有限公司',
          left: 'center'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            animation: false
          }
        },
        grid: {
          right: 250
        },

        toolbox: {
          feature: {
            dataView: {show: true, readOnly: false},
            restore: {},
            saveAsImage: {}
          }
        },
        dataZoom: [
          {
            show: true,
            realtime: true,
            start: 0,
            end: 100,
          },
          {
            type: 'inside',
            realtime: true,
            start: 30,
            end: 70,
          }
        ],
        xAxis:
          {
            type: 'category',
            data: timeData
          }
        ,
        yAxis:
          {
            name: '流量(m^3/s)',
            type: 'value',
          },
        series:data
      };
      option && myChart.setOption(option);

    }
  },
  mounted() {
    this.axios
      .get('http://localhost:80/static/twitterAPI.json')
      .then(response => (
        this.twitterAPI = response.data.LGA,
          this.myEcharts2()
      ));

  }

}
</script>

<style scoped>

</style>
