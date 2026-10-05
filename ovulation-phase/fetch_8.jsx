// PRACTICAL 8
// AIM: Fetch the API data & render the list on React App

//   npm create vite@latest my-app -- --template react
//   cd my-app
//   npm install
//   npm run dev          -> opens at http://localhost:5173
//
//   Each practical below replaces src/App.jsx (Vite uses .jsx, notebook says .js).
//   Extra packages are listed in each practical's setup.

// ---- SETUP ----
//   No extra packages (uses built-in fetch + free API jsonplaceholder).
//   Replace src/App.jsx with the code below.

import "./App.css";
import { useEffect, useState } from "react";

function App() {
  const [users, setUsers] = useState([]);

  // runs once after first render
  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((data) => {
        setUsers(data);
      })
      .catch((err) => console.log(err));
  }, []);

  // FIX: removed the unused logo import and the unreachable second return
  return (
    <div style={{ padding: "20px" }}>
      <h1>User List</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <h3>{user.name}</h3>
            <p>Email: {user.email}</p>
            <p>City: {user.address.city}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
