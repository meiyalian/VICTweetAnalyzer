<template>
  <div class="Echarts" style="height: 100%">
    <div id="count" style="width: 100%;height:100%;"></div>
    
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "twitterEmoji",
  methods:{
    myEcharts(){

      var chartDom = document.getElementById('count');
      var myChart = echarts.init(chartDom);
      var option;


      var data = genData(this.twitterAPI);

      var colors = [ '#BFD8D2'];

      option = {
          color:colors,

    title: {
        text: 'The Top Five Emoji In Vic',
        
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross'
        }
    },
    
    
    xAxis: {
        type: 'value',
        //boundaryGap: [0, 0.01],
        
    },
    yAxis: {
        type: 'category',
        data: data.legendData,
        axisLabel: {
            show: true,
                textStyle: {
                fontSize : 25      //change the front size
                }
            },
    },
    series: [
        {
            name: 'Number',
            type: 'bar',
            itemStyle:{
                barBorderRadius: [0,5,5,0],
                normal: {
                    label: {
                        show: true, //show
                        position: 'right', 
                        textStyle: { 
                            color: 'black',
                            fontSize: 16
                        }
                    }
                }
                
                },
            barWidth:60,    
            data: data.seriesData
            
        },
        
    ]
};

option && myChart.setOption(option);


      function genData(twitterAPI) {
        var legendData = [];
        var seriesData = [];

        // for (var obj in twitterAPI){
        //   legendData.push(twitterAPI[obj].emojicode);
        //   seriesData.push({
        //     name: twitterAPI[obj].emojicode,
        //     value: twitterAPI[obj].number ,

        //   }
        //   );
          

        // }



        legendData.push(twitterAPI[4].emojicode);
          seriesData.push({
            name: twitterAPI[4].emojicode,
            value: twitterAPI[4].number ,

          }
          );
          legendData.push(twitterAPI[3].emojicode);
          seriesData.push({
            name: twitterAPI[3].emojicode,
            value: twitterAPI[3].number ,

          }
          );
          legendData.push(twitterAPI[2].emojicode);
          seriesData.push({
            name: twitterAPI[2].emojicode,
            value: twitterAPI[2].number ,

          }
          );
          legendData.push(twitterAPI[1].emojicode);
          seriesData.push({
            name: twitterAPI[1].emojicode,
            value: twitterAPI[1].number ,

          }
          );



        legendData.push(twitterAPI[0].emojicode);
          seriesData.push({
            name: twitterAPI[0].emojicode,
            value: twitterAPI[0].number ,

          }
          );

        return {
          legendData: legendData,
          seriesData: seriesData,
          
        };
      }

      



      option && myChart.setOption(option);
    },
    },

    

  mounted() {
    var that = this;
    const path = '/api/getTopFiveEmoji';
    that.axios.get(path).then(function(response){
        var msg = response.data.data;
        that.twitterAPI = msg;
        that.myEcharts()
          

    })

  }
}
</script>

<style scoped>

</style>
