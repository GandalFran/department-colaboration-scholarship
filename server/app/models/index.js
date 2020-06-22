const mongoose = require('mongoose');
const config = require('../config/db.config');

const db = {};
db.mongoose = mongoose;
db.url = config.mongoUrl;
db.news = require('./news.model')(mongoose);
db.entities = require('./entitites.model')

module.exports = db;
