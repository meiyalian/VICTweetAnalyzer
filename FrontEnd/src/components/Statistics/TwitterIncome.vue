<template>
  <div class="Echarts" style="height: 100%">
    <div ref="positive" style="width: 100%;height:100%;"></div>
    <div id="negative" style="width: 100%;height:100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "twitterIncome",
  methods:{
    myEcharts(){

      var chartDom = document.getElementById('main');
      var myChart = echarts.init(this.$refs.positive);
      var option;


      var data = genData(this.twitterAPI);
      console.log(data);

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
            text:"The Relation Between Income And Positive Sentiment"
          },
          toolbox: {
              feature: {
                  dataView: {show: true, readOnly: false},
                  restore: {show: true},
                  saveAsImage: {show: true}
              }
          },
          legend: {
              data: ['Average Income', 'Positive (%)', 'Negative']
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
                  name: 'Average Income',

                  axisLabel: {
                      formatter: '{value} AUD'
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
                  name: 'Average Income',
                  type: 'bar',
                  itemStyle:{barBorderRadius: [3,3,0,0]},
                  data: data.incomeData


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
        var incomeData = [];

       

        for (var obj in twitterAPI){
          legendData.push(twitterAPI[obj].area);
          
          positiveScore.push(
            {
              name: twitterAPI[obj].area,
              value: twitterAPI[obj].positive
            }
          );
          negativeScore.push(
            {
              name: twitterAPI[obj].area,
              value: twitterAPI[obj].negative
            }
          );
          incomeData.push(
            {
              name: twitterAPI[obj].area,
              value: twitterAPI[obj].income_average
            }
          );

        }
        return {
          legendData: legendData,
          seriesData: seriesData,
          positiveScore : positiveScore,
          negativeScore : negativeScore,
          incomeData:incomeData
        };
      }



      option && myChart.setOption(option);
    },
    myEchart2(){
      var chartDom = document.getElementById('negative');
      var myChart = echarts.init(chartDom);
      var option;


      var data = genData(this.twitterAPI);

      var colors = [ '#E5E338','#008F95'];

      option = {
          color: colors,
          title:{
            text:"The Relation Between Income And Negative Sentiment"
          },

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
              data: ['Average Income', 'Positive (%)', 'Negative (%)']
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
                  name: 'Average Income',

                  axisLabel: {
                      formatter: '{value} AUD'
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
                  name: 'Average Income',
                  type: 'bar',
                  itemStyle:{barBorderRadius: [3,3,0,0]},
                  data: data.incomeData


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
        var incomeData = [];

        for (var obj in twitterAPI){
          legendData.push(twitterAPI[obj].area);
          
          positiveScore.push(
            {
              name: twitterAPI[obj].area,
              value: twitterAPI[obj].positive
            }
          );
          negativeScore.push(
            {
              name: twitterAPI[obj].area,
              value: twitterAPI[obj].negative
            }
          );
          incomeData.push(
            {
              name: twitterAPI[obj].area,
              value: twitterAPI[obj].income_average
            }
          );

        }
        return {
          legendData: legendData,
          seriesData: seriesData,
          positiveScore : positiveScore,
          negativeScore : negativeScore,
          incomeData:incomeData
        };
      }



      option && myChart.setOption(option);

    }
  },
  mounted() {
    var that = this;
    const path = '/api/incomesentiment';
    that.axios.get(path).then(function(response){        
       var msg =response.data.data;
        console.log(response.data);
        that.twitterAPI = msg;
        that.myEcharts();
        that.myEchart2()
          

    }
    
    
    )

  }
}
</script>

<style scoped>

</style>
