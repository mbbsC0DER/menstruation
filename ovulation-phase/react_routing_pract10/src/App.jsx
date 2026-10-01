// PRACTICAL 10
// AIM: Implement routing using React Router

//   npm create vite@latest my-app -- --template react
//   cd my-app
//   npm install
//   npm run dev          -> opens at http://localhost:5173
//
//   Each practical below replaces src/App.jsx (Vite uses .jsx, notebook says .js).
//   Extra packages are listed in each practical's setup.

// ---- SETUP ----
//   npm install react-router-dom
//   Create folder src/pages/ with Home.jsx, About.jsx, Contact.jsx (below)
//   Replace src/App.jsx with the code below.
//   Click the links: the URL changes without a page reload.

import "./App.css";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> {" | "}
        <Link to="/about">About</Link> {" | "}
        <Link to="/contact">Contact</Link>
      </nav>
      <hr />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
