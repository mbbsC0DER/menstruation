const mongoose = require("mongoose");

module.exports = mongoose.model("File", {
  filename: String,
  contentType: String,
  data: Buffer,
});
