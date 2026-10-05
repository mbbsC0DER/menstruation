const express = require("express");
const multer = require("multer");
const File = require("../models/File");

const router = express.Router();
const upload = multer({ storage: multer.memoryStorage() }); // keeps file in RAM as buffer

// UPLOAD  (form-data field name must be "file")
router.post("/upload", upload.single("file"), async (req, res) => {
  try {
    if (!req.file) return res.status(400).json({ message: "No file uploaded" });

    const f = await new File({
      filename: req.file.originalname,
      contentType: req.file.mimetype,
      data: req.file.buffer,
    }).save();

    res.json({ message: "File uploaded successfully", id: f._id });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// VIEW / DOWNLOAD
router.get("/:id", async (req, res) => {
  try {
    const f = await File.findById(req.params.id);
    if (!f) return res.status(404).send("File not found");
    res.contentType(f.contentType).send(f.data);
  } catch (err) {
    res.status(400).send("Invalid id");
  }
});

module.exports = router;
