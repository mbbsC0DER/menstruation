// PRACTICAL 4
// AIM: Create a custom Node.js module, package it using npm, test it locally
// and publish it to the npm registry so it can be installed and used in
// other Node.js projects.

// ---- STEP-BY-STEP COMMANDS ----
//   1) mkdir user-module && cd user-module
//   2) npm init -y
//        -> edit package.json: "name" must be UNIQUE on npm. Use a scoped name:
//           "name": "@yournpmusername/user-module"
//           "main": "index.js"
//   3) Create index.js (below) and test.js (below)
//   4) Test locally:               node test.js
//   5) Test as a real package locally (from ANOTHER folder):
//        cd ../other-project
//        npm init -y
//        npm install ../user-module          (or: npm link in module, npm link @yournpmusername/user-module in project)
//   6) Publish:
//        npm login                            (create a free account at npmjs.com first)
//        npm publish --access public          (--access public is needed for scoped names)
//   7) Use it anywhere:
//        npm install @yournpmusername/user-module
//        const userModule = require("@yournpmusername/user-module");
//   8) To publish an update: bump version (npm version patch) then npm publish again.

function addUser(name, email) {
  return {
    name,
    email,
    message: "User added successfully",
  };
}

function displayUser(user) {
  return `Name: ${user.name}
Email: ${user.email}
Status: ${user.message}`;
}

module.exports = { addUser, displayUser };
