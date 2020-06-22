module.exports = (mongoose) => {
  const schema = mongoose.Schema({
    sentiment: {
      neg: Number,
      pos: Number,
      compound: Number,
      neu: Number
    },
    author: String,
    title: String,
    url: String
  });

  return mongoose.model('newsitems', schema);
};
