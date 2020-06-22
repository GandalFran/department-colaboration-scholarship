module.exports = (app) => {
  const router = require('express').Router();
  const news = require('../controllers');
  router.get('/entities', news.getNews);
  router.get('/news', news.getEntities);
  app.use('/api/v1', router);
};
