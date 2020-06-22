<template>
  <v-app>
    <v-content> 
      <v-container
        fluid
      >

    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="12"
        md="10"
      >
        <v-card
          raised
        >
        <entities :entities="entitiesItems"/>
        </v-card>
      </v-col>
    </v-row>

    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="12"
        md="10"
      >
        <v-card
          raised
        >
        <v-data-table
          v-bind="newsItems"
          :v-bind="newsItems"
          :items-per-page="10"
          :headers="headers"
          :items="newsItems"
        />
        </v-card>
      </v-col>
    </v-row>

  </v-container>

    </v-content>
  </v-app>
</template>

<script>
import axios from 'axios'
import Entities from '@/components/entities.vue'


export default {
  name: 'App',

  components: {
    Entities,
  },

  data () {
    return {
      newsItems: [],
      entitiesItems: [],
      headers: [
        {
          sortable: true,
          text: 'title',
          value: 'title',
          align: 'right',
        },
        {
          sortable: true,
          text: 'author',
          value: 'author',
          align: 'right',
        },
        {
          sortable: true,
          text: 'sentiment',
          value: 'sentiment',
        },
        {
          sortable: false,
          text: 'url',
          value: 'url',
        },
      ],
    }
  },

  mounted () {
    this.retrieveNews()
    this.retrieveEntitites()
  },

  methods: {
    retrieveNews() {
      const uri = 'http://localhost:5000/news'
      axios.get(uri, {
      }).then(response => {
        this.newsItems = response.data
      }).catch(e => {
        console.error(e)
      })
    }, 
    retrieveEntitites() {
      const uri = 'http://localhost:5000/entities'
      axios.get(uri, {
      }).then(response => {
        this.newsItems = response.data
      }).catch(e => {
        console.error(e)
      })
    },
  },
};
</script>
