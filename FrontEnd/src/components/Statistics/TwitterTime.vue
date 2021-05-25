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
    myEcharts(){
      var chartDom = document.getElementById('twitterTime');
      var myChart = echarts.init(chartDom);
      var option;
      var data = genData(this.twitterAPI);

      var timeData = ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00',
                        '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',];


      setTimeout(function () {

        option = {
          title: {
            text: 'The Relation Between Time And Sentiment'
          },
          legend: {
            data: ['Positive Sentiment', 'Negative Sentiment'],
            top: '48%'
          },
          tooltip: {
            trigger: 'axis',
            showContent: true
          },
          xAxis:
            {
              type: 'category',
              data: timeData,
              name: 'time'
            },
          yAxis:
            {
            type: 'value',
            name: 'Percentage',
            axisLabel: {
              formatter: '{value} %'
            },
            },
          grid: {top: '55%'},
          series: [
            {type: 'line', name:'Positive Sentiment',smooth: true, seriesLayoutBy: 'row', data:data.positiveScore},
            {type: 'line', name:'Negative Sentiment',smooth: true, seriesLayoutBy: 'row', data:data.negativeScore},
            {
              type: 'pie',
              id: 'pie',
              radius: '35%',
              center: ['50%', '25%'],
              data: data.top_five_emojis[0],
              label: {
                formatter: '{b}: {@0} ({d}%)'
              },
            }
          ]
        };

        myChart.on('updateAxisPointer', function (event) {
          var xAxisInfo = event.axesInfo[0];
          if (xAxisInfo) {
            var dimension = xAxisInfo.value;
            console.log(dimension)
            myChart.setOption({
              series: {
                id: 'pie',
                label: {
                  formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                },
                data: data.top_five_emojis[dimension],
                encode: {
                  value: dimension,
                  tooltip: dimension
                }
              }
            });
          }
        });
        myChart.setOption(option);

      });

      function genData(twitterAPI) {
        var positiveScore = [];
        var negativeScore = [];
        var top_five_emojis = [];

        for (var obj in twitterAPI){

          positiveScore.push(
            {
              value: twitterAPI[obj].positive
            }
          );
          negativeScore.push(
            {
              value: twitterAPI[obj].negative
            }
          );
          top_five_emojis.push([
            {value: twitterAPI[obj].top_five_emojis[0].number, name: twitterAPI[obj].top_five_emojis[0].emojicode},
            {value: twitterAPI[obj].top_five_emojis[1].number, name: twitterAPI[obj].top_five_emojis[1].emojicode},
            {value: twitterAPI[obj].top_five_emojis[2].number, name: twitterAPI[obj].top_five_emojis[2].emojicode},
            {value: twitterAPI[obj].top_five_emojis[3].number, name: twitterAPI[obj].top_five_emojis[3].emojicode},
            {value: twitterAPI[obj].top_five_emojis[4].number, name: twitterAPI[obj].top_five_emojis[4].emojicode},
            ]
          );
        }
        return {
          positiveScore : positiveScore,
          top_five_emojis : top_five_emojis,
          negativeScore : negativeScore,
        };
      }

      option && myChart.setOption(option);

    },
  },
  mounted() {
    this.axios
      .get('http://localhost:80/static/time.json')
      .then(response => (
        this.twitterAPI = response.data.data,
          this.myEcharts()
      ));

  }

}
</script>

<style scoped>

</style>
