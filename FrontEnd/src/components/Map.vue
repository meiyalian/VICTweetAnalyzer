<template>
  <div id="map"></div>
</template>

<script>
import MapStatistics from "./MapStatistics";
import Vue from 'vue'
const MapStatisticsItem = Vue.extend(MapStatistics)

import mapboxgl from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";
export default {
  name: 'Map',
  mounted() {
    this.axios
      .get('http://localhost:80/static/twitterAPI.json')
      .then(response => (
        this.twitterAPI = response.data.LGA,
          this.init()
      ));
  },
  methods: {
    init() {
      var twitterAPI = this.twitterAPI;
      this.mbgl.accessToken = 'pk.eyJ1IjoiYXJ2aW45NyIsImEiOiJja28xaGN1NW0wbHJ2Mnhtc2t4cjVvMnEzIn0.QQq7SIEs6bI7RfRdPxsBFQ';
      let map = new this.mbgl.Map({
        container: 'map',
        style: 'mapbox://styles/arvin97/cko1jopxz0rhu17qs49lulfk7',
      });

      map.on("load", function () {
        map.addSource("LGA", {
          type: "geojson",
          data:
            "http://localhost:80/static/LGA.geojson",
        });
        map.addLayer({
          id: "LGA",
          type: "fill",
          source: "LGA",
          layout: {},
          paint: {
            "fill-color": "#088",
            "fill-opacity": 0.5
          }
        });
        map.on("click", "LGA", function (e) {
            var ABB_NAME =  e.features[0].properties.ABB_NAME
            new mapboxgl.Popup()
              .setMaxWidth('500px')
              .setLngLat(e.lngLat)
              .setHTML(
                '<div id="base-detail"></div>'
              ).addTo(map);
            new MapStatisticsItem({
                propsData: {
                  ABB_NAME: ABB_NAME
                }
              }).$mount('#base-detail')
            }.bind(this)
        );
      });
    },
  },

}






</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#map {
  height: 100%;
}

#mapboxgl-canvas{
  width: 100%;
}

#mapboxgl-ctrl mapboxgl-ctrl-attrib{
  display: none;
}
</style>
