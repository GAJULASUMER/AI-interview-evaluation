import React, { useState } from "react";
import { askChatbot } from "../services/api.js";

const Chatbot = () => {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  const handleAsk = async () => {
    const reply = await askChatbot(prompt);
    setResponse(reply);
  };

  return (
    <section>
      <h1>Ask HR Anything</h1>
      <textarea
        rows={4}
        style={{ width: "100%" }}
        placeholder="Ask your HR question..."
        value={prompt}
        onChange={(event) => setPrompt(event.target.value)}
      />
      <button onClick={handleAsk} style={{ marginTop: "12px" }}>
        Ask
      </button>
      {response && (
        <div style={{ marginTop: "16px" }}>
          <strong>HR Response</strong>
          <p>{response}</p>
        </div>
      )}
    </section>
  );
};

export default Chatbot;
