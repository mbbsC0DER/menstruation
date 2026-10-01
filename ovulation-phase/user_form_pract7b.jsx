// PRACTICAL 7(b)   (number unclear in notebook)
// AIM: Create & validate the user form in React

//   npm create vite@latest my-app -- --template react
//   cd my-app
//   npm install
//   npm run dev          -> opens at http://localhost:5173
//
//   Each practical below replaces src/App.jsx (Vite uses .jsx, notebook says .js).
//   Extra packages are listed in each practical's setup.

// ---- SETUP ----
//   No extra packages. Replace src/App.jsx with the code below.
//   Valid password example:  Abcdef1@x

import { useState } from "react";

function App() {
  const [form, setForm] = useState({
    firstname: "",
    lastname: "",
    mobile: "",
    age: "",
    email: "",
    password: "",
  });

  const change = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const validate = (e) => {
    e.preventDefault();
    const { firstname, email, password } = form;

    if (!firstname) return alert("Invalid form, First Name can not be empty");
    if (!email) return alert("Invalid form, Email can not be empty");
    // FIX: "< 8" matches the message (>= 8 characters allowed); notes had "<= 8"
    if (password.length < 8)
      return alert("Invalid form, Password must contain greater than or equal 8 characters");
    if (!/[A-Z]/.test(password))
      return alert("Invalid form, 0 upper case character in password");
    if (!/[a-z]/.test(password))
      return alert("Invalid form, 0 lower case character in password");
    if (!/[0-9]/.test(password))
      return alert("Invalid form, 0 digit character in password");
    if (!/[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]/.test(password))
      return alert("Invalid form, 0 special character in password");

    alert("Form submitted successfully");
  };

  return (
    <div className="main">
      <form onSubmit={validate}>
        {["firstname", "lastname", "mobile", "age", "email", "password"].map((x) => (
          <div key={x}>
            <input
              name={x}
              type={x === "password" ? "password" : "text"}
              placeholder={x}
              value={form[x]}
              onChange={change}
            />
            <br />
          </div>
        ))}
        <br />
        <button>Submit</button>
      </form>
    </div>
  );
}

export default App;
