// PRACTICAL 2
// AIM: Perform File (image / doc) upload operation by using MongoDB

// ---- SETUP ----
//   mkdir file-upload && cd file-upload
//   npm init -y
//   npm install express mongoose multer
//
// Folder structure:
//   models/File.js
//   routes/fileRoutes.js
//   server.js
//
// Run:   node server.js
// Test:
//   Upload  : curl -F "file=@C:/path/to/image.png" http://localhost:3000/files/upload
//             (or Postman: POST, Body -> form-data, key "file" type File)
//   Download: open http://localhost:3000/files/<id> in browser
// Note: files are stored inside MongoDB as Buffer (max 16 MB per document).

const express = require("express");
const mongoose = require("mongoose");

const app = express();

mongoose
  .connect("mongodb://127.0.0.1:27017/fileDB")
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log(err));

app.use("/files", require("./routes/fileRoutes"));

app.listen(3000, () => console.log("Server running on port 3000"));
