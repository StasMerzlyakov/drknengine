/**
 * DRAKON elements library
 */

//SVG = typeof(SVG) == 'undefined' ? SVG() : SVG;

//////////////////////////////////////////////////
// Vertical line
//////////////////////////////////////////////////

/*
SVG.VLine = class extends SVG.Shape {

}


// Extend SVG container
SVG.extends(SVG.Container, {
    // Add vline method
    vline: function(height){
        return this.put(new SVG.VLine).size(height)
    }
})

/ * set default * /
settings:  {
    x : 10,
        y : 10,
        size : 20,
        width: 1,
        color: '#000000'
},
*/

// Add time management methods to clock
SVG.VLine = class extends SVG.Line {

    // default values
   /* settings = {
        x : 10,
        y : 10,
        height : 20,
        width: 1,
        color: '#000000'
    } */

    create(x, y, height) {

        return this.attr({
            x : x,
            y : y,
            height: height,
            x1: x,
            x2: x,
            y1: y,
            y2: y + height
            })


            /*
        / * merge options * /
        options = options || {}
        for (let i in options)
            this.settings[i] = options[i]
        let st = this.settings
        this.line = SVG.line(st.x, st.y, st.x, st.y + st.height)
        return this */
    }

    plot(x, y, height) {
        super.plot(x,y, x, y+height)
    }

    move(x, y){
        this.x = x
        this.y = y
        this.plot(x, y, this.height)
        return this
    }

    resize(dh) {
        this.height = this.height + dh
        this.plot(this.x, this.y, this.height)
        return this
    }
    extend(heigth) {
        this.height = heigth
        this.plot(this.x, this.y, this.height)
        return this
    }

};

// Add a method to create a rounded rect
SVG.extend(SVG.Container,  {
    // Create a rounded element
    vline: function(x,y,height) {
        return this.put(new SVG.VLine).create(x,y, height)
    }
})

SVG.Rounded = class extends SVG.Rect{
    // Create method to proportionally scale the rounded corners
    size (width, height) {
        return this.attr({
            width:  width
            , height: height
            , rx:     height / 5
            , ry:     height / 5
        })
    }
}

// Add a method to create a rounded rect
SVG.extend(SVG.Container,  {
    // Create a rounded element
    rounded: function(width, height) {
        return this.put(new SVG.Rounded).size(width, height)
    }
})


