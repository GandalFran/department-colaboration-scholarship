module.exports = (app) => {
  const router = require('express').Router();
  const news = require('../controllers');
  router.get('/news', news.getNews);
  router.get('/entities', news.getEntities);
  app.use('/api/v1', router);
};
