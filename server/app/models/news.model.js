module.exports = (mongoose) => {
  const schema = mongoose.Schema({
    internalId: String,
    news: Array
  });

  return mongoose.model('newsitems', schema);
};
