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
        en: {
            messages: {
                editor_name: 'DRAKON Editor',
		locale: 'Lang',
                schema: 'Schema',
                load: 'Load',
                save: 'Save'
            }
	},
	ru: {
            messages: {
                editor_name: 'Редактор ДРАКОН-схем',
		locale: 'Язык',
                schema: 'Схема',
                load: 'Загрузить',
                save: 'Сохранить'
            }
	}
    }
})


const app = new Vue({
    i18n,
    render: h => h(App),
    data () {
        return {
            file: null,
            langs: ['ru', 'en'] 
	}
    },
    methods: {
	getLocales() {
            return this.langs
	}, 
	setLocale(locale) {
            if (this.langs.contains(locale))
                i18n.locale=locale 
	},
    }
})

app.$mount('#app')


