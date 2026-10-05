// PRACTICAL 7(a)
// AIM: Create TODO list by using React hooks with different components

//   npm create vite@latest my-app -- --template react
//   cd my-app
//   npm install
//   npm run dev          -> opens at http://localhost:5173
//
//   Each practical below replaces src/App.jsx (Vite uses .jsx, notebook says .js).
//   Extra packages are listed in each practical's setup.

// ---- SETUP ----
//   npm install styled-components
//   Replace src/App.jsx with the code below.

import React, { useState } from "react";
import "./App.css";
import styled from "styled-components";

// styled components (names must start with a capital letter)
const Container = styled.div`
  display: flex;
  flex-direction: column; /* FIX: stack items vertically */
  align-items: center;
  text-align: center;
  margin-top: 30px;
`;

const Input = styled.input`
  height: 35px;
  width: 250px;
  padding: 5px;
`;

const Button = styled.button`
  margin: 10px;
  background: #4caf50;
  color: white;
  border: 0;
  padding: 12px 25px;
  border-radius: 4px;
  cursor: pointer;
`;

function App() {
  const [input, setInput] = useState("");
  const [tasks, setTasks] = useState([]);

  const addTask = () => {
    if (!input.trim()) return;
    setTasks([...tasks, { text: input, completed: false }]);
    setInput("");
  };

  const toggle = (i) => {
    setTasks(
      tasks.map((t, x) => (x === i ? { ...t, completed: !t.completed } : t))
    );
  };

  const pending = tasks.filter((t) => !t.completed).length;
  const completed = tasks.length - pending;

  return (
    <Container>
      <h2>Todo List</h2>

      <Input
        placeholder="Enter a task"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <Button onClick={addTask}>Add</Button>

      <p>
        <b>Pending Tasks: {pending}</b>&nbsp;
        <b>Completed Tasks: {completed}</b>
      </p>

      {tasks.map((t, i) => (
        <div key={i}>
          <span style={{ textDecoration: t.completed ? "line-through" : "none" }}>
            {t.text}
          </span>
          <input
            type="checkbox"
            checked={t.completed}
            onChange={() => toggle(i)}
          />
        </div>
      ))}

      <br />
      <Button onClick={() => setTasks([])}>Clear All</Button>
    </Container>
  );
}

export default App;
