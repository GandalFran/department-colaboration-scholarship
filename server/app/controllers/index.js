const mongoose = require('mongoose');
const db = require('../models');
const News = db.news;

module.exports = {
  // GET /news/:id
  getNews: (req, res) => {
    const id = req.params.id;
    News.find({})
      .then((data) => {
        res.send({ news: data });
      })
      .catch((err) => {
        res.send({news: []});
      });
  },
  getEntities: (req, res) => {
    res.send({entities: []});
  }
};
