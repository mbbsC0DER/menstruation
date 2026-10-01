// PRACTICAL (Chat app)
// AIM: Create chat application by using Socket.IO

// The source does not assign a practical number to this chat app.

// ---- SETUP ----
//   mkdir chat-app && cd chat-app
//   npm init -y
//   npm install express socket.io
//
// Folder structure:
//   index.js
//   index.html
//
// Run:   node index.js
// Test:  open http://localhost:3000 in TWO browser tabs and chat between them.

const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

io.on("connection", (socket) => {
  console.log("A user connected:", socket.id);

  socket.on("chat message", (msg) => {
    console.log("Message received:", msg);
    io.emit("chat message", msg); // broadcast to everyone
  });

  socket.on("disconnect", () => {
    console.log("User disconnected:", socket.id);
  });
});

// FIX: notes listened on 8000 but printed 3000 - made consistent
server.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});
