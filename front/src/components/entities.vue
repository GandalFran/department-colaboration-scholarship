<template>
  <v-container
    fluid
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="12"
        md="12"
      >
        <v-card>
          <div
            ref="canvas"
            class="Canvas"
          />
        </v-card>
      </v-col>
      <v-col
        v-show="cache.length > 0"
        v-bind="cache"
        cols="12"
        md="12"
      >
        <v-subheader class="pl-0">
          Select number of entities
        </v-subheader>
        <v-slider
          v-if="cache.length > 0"
          v-model="numEntities"
          v-bind="cache"
          :min="1"
          :max="maxEntities"
          thumb-label
          color="#4DCCBD"
          track-color="#98a398"
          @end="onSliderUpdate"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import * as am4core from '@amcharts/amcharts4/core'
  import am4themesanimated from '@amcharts/amcharts4/themes/animated'
  import * as am4pluginsForceDirected from '@amcharts/amcharts4/plugins/forceDirected'
  export default {
    name: 'Entities',
    props: {
      entities: {
        type: Array,
        required: true,
      }
    },
    data () {
      return {
        cache: [],
        numEntities: 10,
      }
    },
    computed: {
      maxEntities () {
        return (this.cache.length > 0) ? this.cache.length : 1;
      },
    },
    watch: {
      entities: function (newValue) {
        this.mapToChart(newValue)
        this.update()
      },
    },
    methods: {
      onSliderUpdate () {
        this.update(null, false)
      },
      mapToChart (entities) {
        
        console.log(entities)
        const relation = entities[0]
        // build the entity information
        this.cache.push({
          id: this.toId(relation),
          size: relation.relations,
          name: relation.name,
          type: relation.type,
          info: relation.info,
          children: relation.related,
          color: this.toColor(relation),
        })
        
        this.cache.sort(function (e1, e2) {
          return (e1.size === e2.size) ? (e1.relatedEntities.length - e2.relatedEntities.length) : (e2.size - e1.size);
        })

      },
      update () {
        const relations = this.cache.slice(0, this.numEntities)
        const canvas = this.$refs.canvas
        am4core.ready(function () {
          am4core.useTheme(am4themesanimated)
          const chart = am4core.create(canvas, am4pluginsForceDirected.ForceDirectedTree)
          const networkSeries = chart.series.push(new am4pluginsForceDirected.ForceDirectedSeries())

          networkSeries.dataFields.linkWith = 'children'
          networkSeries.dataFields.name = 'name'
          networkSeries.dataFields.id = 'id'
          networkSeries.dataFields.value = 'size'
          networkSeries.dataFields.color = 'color'
          networkSeries.nodes.template.label.text = '{name}'
          networkSeries.fontSize = 8
          networkSeries.linkWithStrength = 0
          networkSeries.data = relations
        })
      },
      toId (e) {
        return `${e.type}_${e.name}`
      },
      toColor (e) {
          // src: https://stackoverflow.com/questions/3426404/create-a-hexadecimal-colour-based-on-a-string-with-javascript
          const hashCode = function (str) { // java String#hashCode
              var hash = 0;
              for (var i = 0; i < str.length; i++) {
                 hash = str.charCodeAt(i) + ((hash << 5) - hash);
              }
              return hash;
          } 
          const intToRGB = function (i){
              var c = (i & 0x00FFFFFF)
                  .toString(16)
                  .toUpperCase();

              return "00000".substring(0, 6 - c.length) + c;
          }

          // aqui lo mio
          const id = this.toId(e)
          const hash = hashCode(id)
          const color = intToRGB(hash)

          return color
      },
    },
  }
</script>

<style scoped>
.Canvas {
  width: 100%;
  height: 500px;
}
</style>
