<template>
	<div class="hello"><div id="svg"></div></div>
</template>

<script>

export default {
  name: 'DrakonEditor',
  inject: ['SVG'],
  data() {
    return {
        size: 600,
        shoulder: 1,
        radiusShift: 2	
    }
  },
  mounted: function() {
      this.$nextTick(function(){
          this.drawPath();
      });
  },
  methods: {
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
      var canvas = this.SVG().addTo('#svg')
          .size(800, 800),
          //.panZoom({ zoomMin: 0.2, zoomMax: 20 }),
        circle = canvas
          .path(d)
          .fill("none")
          .stroke(stroke),
        lineR = canvas
          .line(radiusX, this.size, this.size, this.size)
          .stroke(stroke),
        lineL = canvas.line(0, this.size, radiusXtwo, this.size).stroke(stroke);
      var group = canvas.group();
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
