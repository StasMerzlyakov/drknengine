import { SVG } from '@svgdotjs/svg.js'

export default {
    install: app => {
        app.provide('SVG', SVG)
    }
}


