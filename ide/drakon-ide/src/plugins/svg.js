import { SVG } from '@svgdotjs/svg.js'

export default {
    install: app => {
        app.prototype.$SVG = SVG
    }
}


