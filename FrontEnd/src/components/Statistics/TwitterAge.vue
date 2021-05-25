<template>
  <div class="Echarts" style="height: 100%">
    <div ref="positive" style="width: 100%;height:100%;"></div>
    <div ref="negative" style="width: 100%;height:100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "twitterAge",
  methods:{
    myEcharts(){
      var myChart = echarts.init(this.$refs.positive);
      var option;


      var data = genData(this.twitterAPI);

       var colors = [ '#E5E338', '#E24E42','#008F95'];

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
          title:{
            text:"The Relation Between Age And Positive Sentiment"
          },
          toolbox: {
              feature: {
                  dataView: {show: true, readOnly: false},
                  restore: {show: true},
                  saveAsImage: {show: true}
              }
          },
          legend: {
              data: ['Average Age', 'Positive', 'Negative']
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
                  name: 'Average Age',

                  axisLabel: {
                      formatter: '{value} years old'
                  }
              },
              {
                  type: 'value',
                  name: 'Percentage',

                  axisLabel: {
                      formatter: '{value} %'
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
                  name: 'Average Age',
                  type: 'bar',
                  itemStyle:{barBorderRadius: [3,3,0,0]},
                  data: data.ageData


              },

              {
                  name: 'Positive',
                  type: 'line',
                  smooth: true,
                  yAxisIndex: 1,
                  data: data.positiveScore

              },
              
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
              value: twitterAPI[obj].age_distribution[0].medium_age
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
      var chartDom = document.getElementById('main');
      var myChart = echarts.init(this.$refs.negative);
      var option;


      var data = genData(this.twitterAPI);

      var colors = [ '#E5E338','#008F95'];

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
          title:{
            text:"The Relation Between Age And Negative Sentiment"
          },
          toolbox: {
              feature: {
                  dataView: {show: true, readOnly: false},
                  restore: {show: true},
                  saveAsImage: {show: true}
              }
          },
          legend: {
              data: ['Average Age', 'Positive', 'Negative']
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
                  name: 'Average Age',

                  axisLabel: {
                      formatter: '{value} years old'
                  }
              },
              {
                  type: 'value',
                  name: 'Percentage',

                  axisLabel: {
                      formatter: '{value} %'
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
                  name: 'Average Age',
                  type: 'bar',
                  itemStyle:{barBorderRadius: [3,3,0,0]},
                  data: data.ageData


              },

              
              {
                  name: 'Negative',
                  type: 'line',
                  smooth: true,
                  yAxisIndex: 1,
                  data: data.negativeScore

              },
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
              value: twitterAPI[obj].age_distribution[0].medium_age
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

    }
  },

  

  mounted() {
    this.axios
      .get('http://localhost:80/static/twitterAPI.json')
      .then(response => (
        this.twitterAPI = response.data.LGA,
          // console.log(this.twitterAPI),
          this.myEcharts(),
          this.myEcharts2()
      ));

  }
}
</script>

<style scoped>

</style>
