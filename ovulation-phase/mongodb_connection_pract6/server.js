// PRACTICAL 6
// AIM: Connect Node.js with MongoDB

// ---- SETUP ----
//   mkdir node-mongo && cd node-mongo
//   npm init -y
//   npm install express mongoose body-parser
//
//   This practical REUSES from Practical 1:
//     models/User.js
//     routes/userRoutes.js
//   Copy both into this folder (same structure), then create server.js below.
//
//   Run:   node server.js
//   Test:  POST/GET http://localhost:3000/users  (see Practical 1 curl examples)
//   Verify data in Mongo shell:  mongosh -> use studentDB -> db.users.find()

const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser"); // (express.json() does the same job)

const app = express();

app.use(bodyParser.json());

mongoose
  .connect("mongodb://127.0.0.1:27017/studentDB")
  .then(() => console.log("Mongodb connected."))
  .catch((err) => console.log(err));

app.use("/users", require("./routes/userRoutes"));

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
