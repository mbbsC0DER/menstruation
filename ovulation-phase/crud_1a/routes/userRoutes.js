const express = require("express");
const User = require("../models/User");

const router = express.Router();

// CREATE
router.post("/", async (req, res) => {
  try {
    const saved = await new User(req.body).save();
    res.status(201).json(saved);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// READ ALL
router.get("/", async (req, res) => {
  try {
    res.json(await User.find());
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// READ ONE
router.get("/:id", async (req, res) => {
  try {
    const u = await User.findById(req.params.id);
    if (!u) return res.status(404).json({ message: "User not found" });
    res.json(u);
  } catch (err) {
    res.status(400).json({ message: "Invalid id" });
  }
});

// UPDATE  ({ new: true } returns the updated document)
router.put("/:id", async (req, res) => {
  try {
    const u = await User.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!u) return res.status(404).json({ message: "User not found" });
    res.json(u);
  } catch (err) {
    res.status(400).json({ message: "Invalid id" });
  }
});

// DELETE
router.delete("/:id", async (req, res) => {
  try {
    const u = await User.findByIdAndDelete(req.params.id);
    if (!u) return res.status(404).json({ message: "User not found" });
    res.json({ message: "User deleted successfully" });
  } catch (err) {
    res.status(400).json({ message: "Invalid id" });
  }
});

module.exports = router;
