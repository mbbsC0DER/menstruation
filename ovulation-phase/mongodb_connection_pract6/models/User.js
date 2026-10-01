const mongoose = require("mongoose");

const User = mongoose.model("User", {
  name: String,
  age: Number,
  email: String,
});

module.exports = User;
