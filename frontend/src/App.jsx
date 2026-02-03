import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Dashboard from "./pages/Dashboard.jsx";
import Practice from "./pages/Practice.jsx";
import Interview from "./pages/Interview.jsx";
import Chatbot from "./pages/Chatbot.jsx";

const App = () => {
  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: "24px" }}>
      <header style={{ display: "flex", gap: "16px", marginBottom: "24px" }}>
        <Link to="/">Dashboard</Link>
        <Link to="/practice">Practice Mode</Link>
        <Link to="/interview">Interview</Link>
        <Link to="/chatbot">Ask HR</Link>
      </header>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/practice" element={<Practice />} />
        <Route path="/interview" element={<Interview />} />
        <Route path="/chatbot" element={<Chatbot />} />
      </Routes>
    </div>
  );
};

export default App;
