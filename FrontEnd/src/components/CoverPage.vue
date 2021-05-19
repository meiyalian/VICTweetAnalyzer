<template>

<div id="cover">
  <div>
    <p class="title">COMP90024 - CLUSTER AND CLOUD COMPUTING</p>
    <p class="title">ASSIGNMENT TWO</p>
    <p class="group">Group Member</p>
    <p>Meiya Lian</p>
    <p>Jiaying Wang</p>
    <p>Yuqi Ma</p>
    <p>Xiangwen Deng</p>
    <p>Zixin Wang</p>
    <el-button type="primary" round @click="$router.push({path:'Main'})">Start</el-button>
  </div>
</div>

</template>

<script>
export default {
  name: "CoverPage"
}
</script>

<style scoped>

#cover{
  background: url("http://localhost:80/static/background.jpg") center no-repeat;
  background-size: 100% 100%;
  height: 100%;
  width: 100%;
}
#cover div{
  position: absolute;
  left: 50%;
  margin-left: -400px;
  top: 50%;
  margin-top: -160px;
  width: 800px;
  height: 200px;
  text-align:center;
}
.title{
  font-size: 28px;
}

.group{
  font-size: 22px;
}
p{
  color: whitesmoke;
}

</style>
