// PRACTICAL 3
// AIM: Perform following operations in Node.js:
// a) Reading a file   b) Writing a file

// ---- SETUP ----
//   mkdir fs-demo && cd fs-demo
//   Create a file named input.txt in the same folder with any text in it
//   (e.g. "This is my input file").
//   Run:   node files_3.js
//   Result: output.txt is created, and input.txt contents are printed.

const fs = require("fs");

// b) WRITE a file
fs.writeFile("output.txt", "Hello students!\nWelcome to Node.js.", (err) => {
  if (err) {
    console.log("Error writing file.");
  } else {
    console.log("File written successfully.");
  }

  // a) READ a file (runs after writing completes)
  fs.readFile("input.txt", "utf8", (err, data) => {
    if (err) {
      console.log("Error reading file.");
    } else {
      console.log("\nContents of input.txt:");
      console.log(data);
    }
  });
});
