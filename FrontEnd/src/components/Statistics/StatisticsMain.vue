<template>
  <el-container>
    <el-header style="width: 100%; margin-bottom: 10px;padding-left: 0">
      <el-menu
               :default-active="this.$router.path"
               router
               default-active="/twitterinfo"
               class="el-menu-demo"
               mode="horizontal"
               @select="handleSelect">
        <!-- <el-menu-item index="/twitterpie">TwitterAPI-Pie</el-menu-item>
        <el-menu-item index="/twitterchart">TwitterAPI-Chart</el-menu-item> -->
        <el-menu-item index="/twitterinfo">Tweet-Amount</el-menu-item>
        <el-menu-item index="/twitteremoji">Top-Five-Emoji</el-menu-item>
        <el-menu-item index="/twittertime">Time&Sentiment</el-menu-item>
        <el-menu-item index="/twitterage">Age&Sentiment</el-menu-item>
        <el-menu-item index="/twitterincome">Income&Sentiment</el-menu-item>
        <el-menu-item index="/twitterdensity">Population-Density&Sentiment</el-menu-item>
        

        <!-- <el-menu-item index="4" disabled >Aurin</el-menu-item>
        <el-menu-item index="5" disabled>TwitterAPI</el-menu-item>
        <el-menu-item index="6" disabled>Aurin</el-menu-item> -->
      </el-menu>
    </el-header>
    <el-main >
      <router-view/>
    </el-main>
  </el-container>

</template>

<script>
export default {
  name: "StatisticsMain",
  data() {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  },



}
</script>

<style scoped>

</style>
