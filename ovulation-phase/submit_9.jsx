// PRACTICAL 9
// AIM: In React submit the user data by using API

//   npm create vite@latest my-app -- --template react
//   cd my-app
//   npm install
//   npm run dev          -> opens at http://localhost:5173
//
//   Each practical below replaces src/App.jsx (Vite uses .jsx, notebook says .js).
//   Extra packages are listed in each practical's setup.

// ---- SETUP ----
//   No extra packages. Replace src/App.jsx with the code below.
//   jsonplaceholder accepts POST requests but does not really save the data;
//   it replies with the object + a new id (check the browser console).

import { useState } from "react";
import "./App.css";

function App() {
  const [user, setUser] = useState({
    name: "",
    email: "",
    password: "",
  });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setUser({
      ...user,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("https://jsonplaceholder.typicode.com/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(user),
      });

      if (response.ok) {
        const data = await response.json();
        console.log("API Response:", data);
        setMessage("User data submitted successfully!");
        setUser({ name: "", email: "", password: "" });
      } else {
        setMessage("Failed to submit user data.");
      }
    } catch (error) {
      console.error(error);
      setMessage("Something went wrong!");
    }
  };

  return (
    <div>
      <h1>User Registration</h1>
      <form onSubmit={handleSubmit}>
        <label>Name: </label>
        <input
          type="text"
          name="name"
          value={user.name}
          onChange={handleChange}
          required
        />
        <br /><br />

        <label>Email: </label>
        <input
          type="text"
          name="email"
          value={user.email}
          onChange={handleChange}
          required
        />
        <br /><br />

        <label>Password: </label>
        <input
          type="password"  /* FIX: hides the password while typing */
          name="password"
          value={user.password}
          onChange={handleChange}
          required
        />
        <br /><br />

        <button type="submit">Submit</button>
      </form>
      <h3>{message}</h3>
    </div>
  );
}

export default App;
