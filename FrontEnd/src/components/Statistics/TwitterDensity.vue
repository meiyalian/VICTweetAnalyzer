<template>
  <div class="Echarts" style="height: 100%">
    <div ref="positive" style="width: 100%;height:100%;"></div>
    <div ref="negative" style="width: 100%;height:100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "twitterDensity",
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
              text:"The Relation Between Density And Positive Sentiment"

          },
          toolbox: {
              feature: {
                  dataView: {show: true, readOnly: false},
                  restore: {show: true},
                  saveAsImage: {show: true}
              }
          },
          legend: {
              data: ['Population Density', 'Positive (%)', 'Negative (%)']
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
                  name: 'Population Density',

                  axisLabel: {
                      formatter: '{value} '
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
                  name: 'Population Density',
                  type: 'bar',
                  itemStyle:{barBorderRadius: [3,3,0,0]},
                  data: data.densityData


              },
              {
                  name: 'Positive (%)',
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
        var densityData = [];

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
          densityData.push(
            {
              name: twitterAPI[obj].ABB_NAME,
              value: twitterAPI[obj].population_density
            }
          );

        }
        return {
          legendData: legendData,
          seriesData: seriesData,
          positiveScore : positiveScore,
          negativeScore : negativeScore,
          densityData:densityData
        };
      }



      option && myChart.setOption(option);
    },
    myEcharts2(){
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
            text:"The Relation Between Density And Negative Sentiment"
          },
          toolbox: {
              feature: {
                  dataView: {show: true, readOnly: false},
                  restore: {show: true},
                  saveAsImage: {show: true}
              }
          },
          legend: {
              data: ['Population Density', 'Positive', 'Negative (%)']
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
                  name: 'Population Density',

                  axisLabel: {
                      formatter: '{value} '
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
                  name: 'Population Density',
                  type: 'bar',
                  itemStyle:{barBorderRadius: [3,3,0,0]},
                  data: data.densityData


              },
              

              {
                  name: 'Negative (%)',
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
        var densityData = [];

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
          densityData.push(
            {
              name: twitterAPI[obj].ABB_NAME,
              value: twitterAPI[obj].population_density
            }
          );

        }
        return {
          legendData: legendData,
          seriesData: seriesData,
          positiveScore : positiveScore,
          negativeScore : negativeScore,
          densityData:densityData
        };
      }



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
