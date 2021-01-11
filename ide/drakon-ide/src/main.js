import Vue from 'vue'
import App from './App.vue'
import svgJS from '@/plugins/svg.js'
import '@/plugins/bootstrap-vue.js'

Vue.config.productionTip = false
Vue.use(svgJS)

new Vue({
  render: h => h(App)
}).$mount('#app')


