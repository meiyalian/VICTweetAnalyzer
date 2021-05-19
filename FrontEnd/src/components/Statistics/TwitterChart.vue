<template>
  <div class="Echarts" style="width: 100%;height:100%;">
    <div id="twitterAPI_chart" style="width: 100%;height:100%;"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
export default {
  name: "TwitterChart",
  methods:{
    myEcharts(){
      var chartDom = document.getElementById('twitterAPI_chart');
      var myChart = echarts.init(chartDom);
      var option;
      var dataAxis = [];
      var data = [];
      for (var obj in this.twitterAPI){
        dataAxis.push(this.twitterAPI[obj].ABB_NAME);
        data.push(this.twitterAPI[obj].sentiment_score)
      }
      option = {
        title: {
          text: '特性示例：渐变色 阴影 点击缩放',
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow',
            label: {
              show: true
            }
          }
        },
        toolbox: {
          feature: {
            dataView: {show: true, readOnly: false},
            restore: {},
            saveAsImage: {}
          }
        },
        xAxis: {
          data: dataAxis,
          axisLabel: {
            outside: true,
            textStyle: {
              // color: '#fff'
            }
          },
          axisTick: {
            show: false
          },
          axisLine: {
            show: false
          },
          z: 10
        },

        yAxis: {
          name:'sentiment_score',
          axisLine: {
            show: false
          },
          axisTick: {
            show: false
          },
          axisLabel: {
            textStyle: {
              color: '#999'
            }
          }
        },
        dataZoom: [
          {
            type: 'inside'
          },
          {
            show: true,
            start: 0,
            end: 100
          },
          {
            type: 'inside',
            start: 0,
            end: 100
          },
        ],
        series: [
          {
            type: 'bar',
            showBackground: true,
            itemStyle: {
              color: new echarts.graphic.LinearGradient(
                0, 0, 0, 1,
                [
                  {offset: 0, color: '#83bff6'},
                  {offset: 0.5, color: '#188df0'},
                  {offset: 1, color: '#188df0'}
                ]
              )
            },
            emphasis: {
              itemStyle: {
                color: new echarts.graphic.LinearGradient(
                  0, 0, 0, 1,
                  [
                    {offset: 0, color: '#2378f7'},
                    {offset: 0.7, color: '#2378f7'},
                    {offset: 1, color: '#83bff6'}
                  ]
                )
              }
            },
            data: data,
          }
        ]
      };

// Enable data zoom when user click bar.
      var zoomSize = 6;
      myChart.on('click', function (params) {
        console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
        myChart.dispatchAction({
          type: 'dataZoom',
          startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
          endValue: dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
        });
      });
      option && myChart.setOption(option);
    }
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
