// PRACTICAL 1(a)
// AIM: Perform CRUD operations by using Express with MongoDB

// ---- SETUP ----
//   cd crud_1a  (from ovulation-phase)
//   npm init -y
//   npm install express mongoose
//
// Folder structure:
//   crud_1a/
//     models/User.js
//     routes/userRoutes.js
//     server.js
//
// Run:   node server.js
// Test (curl examples):
//   Create : curl -X POST http://localhost:3000/users -H "Content-Type: application/json" -d "{\"name\":\"Amit\",\"age\":21,\"email\":\"amit@gmail.com\"}"
//   Read   : curl http://localhost:3000/users
//   Read 1 : curl http://localhost:3000/users/<id>
//   Update : curl -X PUT http://localhost:3000/users/<id> -H "Content-Type: application/json" -d "{\"age\":22}"
//   Delete : curl -X DELETE http://localhost:3000/users/<id>

const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());

// FIX: use 127.0.0.1 (avoids localhost -> IPv6 issue on Node 17+)
mongoose
  .connect("mongodb://127.0.0.1:27017/studentDB")
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log(err));

app.use("/users", require("./routes/userRoutes"));

// FIX: notes listened on 8000 but printed 3000 - made consistent
app.listen(3000, () => console.log("Server running on port 3000"));
