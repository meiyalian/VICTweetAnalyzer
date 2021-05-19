<template>
  <div class="Echarts" style="height: 100%">
    <div id="main" style="width: 100%;height:100%;"></div>
    <div id="main2" style="width: 100%;height:100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: "Income",
  methods:{
    myEcharts(){

      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom);
      var option;

      var data = genData(87);

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
              data: ['income level', 'positive score', 'negative score']
          },
          xAxis: [
              {
                  type: 'category',
                  axisTick: {
                      alignWithLabel: true
                  },
                  data: ['地区', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
              }
          ],
          yAxis: [
              {
                  type: 'value',
                  name: 'negative score',
                  min: 0,
                  max: 250,
                  position: 'right',
                  offset: 100,                  
                  axisLine: {
                      show: true,
                      lineStyle: {
                          color: colors[0]
                      }
                  },
                  axisLabel: {
                      formatter: '{value} point'
                  }
              },
              {
                  type: 'value',
                  name: 'income level',
                  min: 0,
                  max: 100,
                  position: 'left',
                  axisLine: {
                      show: true,
                      lineStyle: {
                          color: colors[1]
                      }
                  },
                  axisLabel: {
                      formatter: '{value} years old'
                  }
              },
              {
                  type: 'value',
                  name: 'positive score',
                  min: 0,
                  max: 250,
                  position: 'right',
                  axisLine: {
                      show: true,
                      lineStyle: {
                          color: colors[2]
                      }
                  },
                  axisLabel: {
                      formatter: '{value} point'
                  }
              }
          ],
          series: [
              {
                  name: 'negative score',
                  type: 'line',
                  yAxisIndex: 1,
                  data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 75.6, 82.2, 48.7, 18.8, 6.0, 2.3]
              },
              {
                  name: 'income level',
                  type: 'bar',
                  data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 13.6, 46.2, 32.6, 20.0, 6.4, 3.3]
                  
              },
              
              {
                  name: 'positive score',
                  type: 'line',
                  yAxisIndex: 2,
                  data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
              }
          ]
      };



      function genData(count) {
        var nameList = [
          '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闵', '席', '季', '麻', '强', '贾', '路', '娄', '危'
        ];
        var legendData = [];
        var seriesData = [];
        for (var i = 0; i < count; i++) {
          var name = Math.random() > 0.65
            ? makeWord(4, 1) + '·' + makeWord(3, 0)
            : makeWord(2, 1);
          legendData.push(name);
          seriesData.push({
            name: name,
            value: Math.round(Math.random() * 100000)
          });
        }

        return {
          legendData: legendData,
          seriesData: seriesData
        };

        function makeWord(max, min) {
          var nameLen = Math.ceil(Math.random() * max + min);
          var name = [];
          for (var i = 0; i < nameLen; i++) {
            name.push(nameList[Math.round(Math.random() * nameList.length - 1)]);
          }
          return name.join('');
        }
      }

      option && myChart.setOption(option);
    },
    myEcharts2(){

    }
  },
  mounted() {
    this.myEcharts();
  }
}
</script>

<style scoped>

</style>
