// PRACTICAL 5
// AIM: Creating server using Express & handling HTTP methods

// ---- SETUP ----
//   mkdir student-api && cd student-api
//   npm init -y
//   npm install express
//   Run:   node http_5.js
// Test:
//   GET    : curl http://localhost:3000/students
//   GET 1  : curl http://localhost:3000/students/1
//   POST   : curl -X POST http://localhost:3000/students -H "Content-Type: application/json" -d "{\"name\":\"Neha\",\"course\":\"BCA\",\"email\":\"neha@gmail.com\"}"
//   PUT    : curl -X PUT http://localhost:3000/students/1 -H "Content-Type: application/json" -d "{\"course\":\"BSc\"}"
//   DELETE : curl -X DELETE http://localhost:3000/students/1

const express = require("express");
const app = express();
const PORT = 3000;

app.use(express.json());

// in-memory data (resets when server restarts)
let students = [
  { id: 1, name: "Amit Sharma", course: "BCA", email: "amit@gmail.com" },
  { id: 2, name: "Priya Patil", course: "BCA", email: "priya@gmail.com" },
  { id: 3, name: "Rahul Joshi", course: "BCA", email: "rahul@gmail.com" },
];

app.get("/", (req, res) => {
  res.send("Welcome to Student Management API");
});

// GET all
app.get("/students", (req, res) => {
  res.json(students);
});

// GET one
app.get("/students/:id", (req, res) => {
  // FIX: Number() because req.params.id is a string
  const s = students.find((x) => x.id === Number(req.params.id));
  if (s) return res.json(s);
  res.status(404).json({ message: "Student not found" });
});

// POST (create)
app.post("/students", (req, res) => {
  // FIX: max id + 1 avoids duplicate ids after a delete
  const s = {
    id: students.length ? Math.max(...students.map((x) => x.id)) + 1 : 1,
    ...req.body,
  };
  students.push(s);
  res.status(201).json({ message: "Student added successfully", student: s });
});

// PUT (update)
app.put("/students/:id", (req, res) => {
  const s = students.find((x) => x.id === Number(req.params.id));
  if (!s) return res.status(404).json({ message: "Student not found" });
  Object.assign(s, req.body);
  res.json({ message: "Student updated successfully", student: s });
});

// DELETE
app.delete("/students/:id", (req, res) => {
  const i = students.findIndex((x) => x.id === Number(req.params.id));
  if (i === -1) return res.status(404).json({ message: "Student not found" });
  const s = students.splice(i, 1)[0];
  res.json({ message: "Student deleted successfully", student: s });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
