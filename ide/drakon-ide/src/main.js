import Vue from 'vue'
import VueI18n from 'vue-i18n'
import App from './App.vue'
import svgJS from '@/plugins/svg.js'
import '@/plugins/bootstrap-vue.js'

Vue.config.productionTip = false
Vue.use(svgJS)
Vue.use(VueI18n)

const i18n = new VueI18n({
    locale: 'ru',
    messages: {
        'en': {
            messages: {
                editor_name: 'DRAKON Editor',
		locale: 'Lang',

            }

	},
	'ru': {
            messages: {
                editor_name: 'Редактор схем',
		locale: 'Язык'
            }
	}
    }
})


new Vue({
    i18n,
    render: h => h(App),
    data () {
        return { langs: ['ru', 'en'] }
    },
    methods: {
        setLocale (locale) {
            console.log(locale);
            i18n.setLocaleMessage(locale);
        }
    }
}).$mount('#app')


