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
        <v-img
            contain
            src="/img/diaLogo.png"
            max-height="290px"
          />
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
        <entities :entities="entitiesItems"/>
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
      const uri = 'http://localhost:5000/api/v1/news'
      axios.get(uri, {
      }).then(response => {
        const mapSentimentFunction = this.mapSentiment
        this.newsItems = response.data.news.map(function(news){
          news.sentiment = mapSentimentFunction(news.sentiment.compound)
          return news
        })

      }).catch(e => {
        console.error(e)
      })
    }, 
    retrieveEntitites() {
      const uri = 'http://localhost:5000/api/v1/entities'
      axios.get(uri, {
      }).then(response => {
        this.entitiesItems = response.data.entities
      }).catch(e => {
        console.error(e)
      })
    },

    mapSentiment (sentiment) {
      return (sentiment > 0.5) ? 'positive' : ((sentiment < -0.5) ? 'negative' : 'neutral')
    },
  },
};
</script>
