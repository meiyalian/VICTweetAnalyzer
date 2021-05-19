<template>
  <div id="app" style="height: 100%">
    <el-container>
      <el-aside width="200px">
        <el-col style="height: 100%;width: 200px;border-right: #e6e6e6 1px solid">
          <div style="height: 61px;text-align: center;line-height: 61px;color: black;border-bottom: #e6e6e6 1px solid" >
            CCC PROJECT
          </div>
          <el-menu
            :default-active="this.$router.path"
            router
            default-active="/viewmap"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose">
            <el-menu-item index="/viewmap">
              <i class="el-icon-menu"></i>
              <span slot="title">View Map</span>
            </el-menu-item>
            <el-menu-item index="/statisticsmain" >
              <i class="el-icon-menu"></i>
              <span slot="title">View Statistics</span>
            </el-menu-item>
          </el-menu>

        </el-col>
      </el-aside>
      <el-container>
        <el-main>
          <router-view/>
        </el-main>
      </el-container>
    </el-container>


  </div>

</template>

<script>
export default {
  name: "Main",
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style scoped>

</style>
