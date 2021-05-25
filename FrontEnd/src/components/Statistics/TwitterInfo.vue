<template>
  <div class="Echarts" style="height: 100%">
    <div id="count" style="width: 100%;height:100%;"></div>
    
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "twitterInfo",
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
        text: 'The Number Of Tweets',
        
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
        data: ['Total Analysed', 'Total Collected'],
        axisLabel: {
       show: true,
        textStyle: {
          fontSize : 16      //change the front size
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
            barWidth:100,    
            data: data.seriesData
            
        },
        
    ]
};

option && myChart.setOption(option);


      function genData(twitterAPI) {
        
        var seriesData = [twitterAPI.total_analysis,twitterAPI.total_collected];

        return {
          
          seriesData: seriesData,
          
        };
      }



      option && myChart.setOption(option);
    },
    },
  mounted() {
    var that = this;
    const path = '/api/totalcollected';
    that.axios.get(path).then(function(response){
        var msg = response.data.data;
        that.twitterAPI = msg;
        that.myEcharts()
          

    }
    
    
    )
  

  }
}
</script>

<style scoped>

</style>
