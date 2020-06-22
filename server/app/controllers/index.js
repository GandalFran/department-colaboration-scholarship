const mongoose = require('mongoose');
const db = require('../models');
const News = db.news;
const Entities = db.entities;

module.exports = {
  // GET /news/:id
  getNews: (req, res) => {
    const id = req.params.id;
    News.find({'internalId':'aDocument'})
      .then((data) => {
        console.log(data)
        res.send({ news: data[0].news });
      })
      .catch((err) => {
        console.log(err)
        res.send({news: []});
      });
  },
  getEntities: (req, res) => {
    Entities.getEntitites().then(function(data){
      res.send({entities: data});
    })
    .catch((err) => {
      console.log(err)
      res.send({entities: []});
    });
  }
};
