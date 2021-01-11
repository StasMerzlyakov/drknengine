<template>
  <img alt="DRAKON Engine" src="./assets/drakosha104.png">
  <DrakonEditor/>
</template>

<script>
import DrakonEditor from './components/DrakonEditor.vue'

export default {
  name: 'App',
  components: {
    DrakonEditor
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
