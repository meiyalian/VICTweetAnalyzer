<template>
  <div class="Echarts" style="height: 100%">
    <div id="main" style="width: 100%;height:100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "twitterAge",
  methods:{
    myEcharts(){

      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom);
      var option;


      var data = genData(this.twitterAPI);

      var colors = ['#5470C6', '#91CC75', '#EE6666'];

      option = {
          color: colors,

          tooltip: {
              trigger: 'axis',
              axisPointer: {
                  type: 'cross'
              }
          },
          grid: {
              right: '20%'
          },
          toolbox: {
              feature: {
                  dataView: {show: true, readOnly: false},
                  restore: {show: true},
                  saveAsImage: {show: true}
              }
          },
          legend: {
              data: ['average age', 'positive score', 'negative score']
          },
          xAxis: [
              {
                  type: 'category',
                  axisTick: {
                      alignWithLabel: true
                  },
                  data: data.legendData,
              }
          ],
          yAxis: [
              {
                  type: 'value',
                  name: 'average age',

                  axisLabel: {
                      formatter: '{value} years old'
                  }
              },
              {
                  type: 'value',
                  name: 'score',

                  axisLabel: {
                      formatter: '{value} points'
                  }
              },


          ],
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
                  name: 'negative score',
                  type: 'line',
                  yAxisIndex: 1,
                  data: data.negativeScore

              },
              {
                  name: 'average age',
                  type: 'bar',
                  data: data.ageData


              },

              {
                  name: 'positive score',
                  type: 'line',
                  yAxisIndex: 1,
                  data: data.positiveScore

              }
          ]
      };   
  
      function genData(twitterAPI) {
        var legendData = [];
        var seriesData = [];
        var negativeScore = [];
        var positiveScore = [];
        var ageData = [];

        for (var obj in twitterAPI){
          legendData.push(twitterAPI[obj].ABB_NAME);
          seriesData.push({
            name: twitterAPI[obj].ABB_NAME,
            value: twitterAPI[obj].sentiment_score ,

          }
          );
          positiveScore.push(
            {
              name: twitterAPI[obj].ABB_NAME,
              value: twitterAPI[obj].positive
            }
          );
          negativeScore.push(
            {
              name: twitterAPI[obj].ABB_NAME,
              value: twitterAPI[obj].negative
            }
          );
          ageData.push(
            {
              name: twitterAPI[obj].ABB_NAME,
              value: twitterAPI[obj].age
            }
          );

        }
        return {
          legendData: legendData,
          seriesData: seriesData,
          positiveScore : positiveScore,
          negativeScore : negativeScore,
          ageData:ageData
        };
      }

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
    },
    myEcharts2(){

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
