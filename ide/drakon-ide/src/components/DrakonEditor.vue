<template>
    <div class="hello"><div id="svg" ref="svg"></div></div>
</template>

<script>

export default {
    name : 'DrakonEditor',
    data() {
        return {
            size: 600,
            shoulder: 1,
            radiusShift: 2,
            canvas : null,
        }
    },
    mounted: function() {
        this.$nextTick(function(){
            this.canvas = this.$SVG().addTo('#svg').size(800, 800),
            this.drawPath();
        });
    },
    methods: {
        importSvg(svg) {
            this.$refs.svg.innerHTML=''
            this.canvas = this.$SVG('#svg')
            this.canvas.svg(svg)
        },
        exportSvg() {
            return this.canvas.svg()            
        },
        drawPath() {
            var stroke = { color: "grey", width: 5 };
            var sH = this.size / 2,
              shoulder = (this.size / 4) * this.shoulder;
            var preRadius = shoulder * this.radiusShift - shoulder;
            var Radius = Math.sqrt(
              preRadius * preRadius + (sH - shoulder) * (sH - shoulder)
            );
            var q = sH - preRadius;
            var radiusX = sH + Math.sqrt(Radius * Radius - (sH - q) * (sH - q));
            var radiusXtwo = radiusX - (radiusX - sH) * 2;
            var d = [
              "M",
              radiusXtwo,
              this.size,
              "A",
              Radius,
              Radius,
              0,
              0,
              1,
              radiusX,
              this.size
            ].join(" ");
            //creating canvas and starting to creating the geometry
                //.panZoom({ zoomMin: 0.2, zoomMax: 20 }),
            var circle = this.canvas
                .path(d)
                .fill("none")
                .stroke(stroke),
              lineR = this.canvas
                .line(radiusX, this.size, this.size, this.size)
                .stroke(stroke),
              lineL = this.canvas.line(0, this.size, radiusXtwo, this.size).stroke(stroke);
            var group = this.canvas.group();
            group.add(circle);
            group.add(lineR);
            group.add(lineL);
            var groupGf = group.clone();
            groupGf.rotate(90, sH, sH).insertAfter(group);
            var groupGs = groupGf.clone();
            groupGs.rotate(90, sH, sH).insertAfter(groupGf);
            var groupGth = groupGs.clone();
            groupGth.rotate(90, sH, sH).insertAfter(groupGs);

        }
  
    },
    props: {
        msg: String
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
