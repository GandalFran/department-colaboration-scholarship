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
            v-bind="cache"
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
        return (this.cache.length > 0) ? (this.cache.length > 100 ? 100: this.cache.length) : 1;
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
        this.update()
      },
      mapToChart (entities) {
        const toIdFunction = this.toId
        this.cache = entities.map(function(entity){
          console.log(entity)
          return {
            id: toIdFunction(entity),
            size: entity.children.length,
            name: entity.name,
            type: entity.type,
            children: entity.children.map(function(child){
              return toIdFunction({name: child.name, type:child.type })
            })
          }
        }).sort(function (e1, e2) {
          return (e2.size - e1.size);
        })
        console.log(this.cache)

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
          networkSeries.nodes.template.label.text = '{name}'
          networkSeries.fontSize = 8
          networkSeries.linkWithStrength = 0
          networkSeries.data = relations
        })
      },
      toId (e) {
        return `${e.type}_${e.name}`
      }
    },
  }
</script>

<style scoped>
.Canvas {
  width: 100%;
  height: 500px;
}
</style>
