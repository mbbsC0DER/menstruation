const userModule = require("./index");

const user = userModule.addUser("ABC", "ABC@gmail.com");
console.log(userModule.displayUser(user));
