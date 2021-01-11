import { defineComponent, createApp } from 'vue'
import App from './App.vue'
import svgJS from '@/plugins/svg.js'

// export global Vue
export default defineComponent({

})
const app = createApp(App)

app.use(svgJS)
app.mount('#app')
