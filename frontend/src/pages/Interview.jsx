import React, { useState } from "react";
import { submitInterview } from "../services/api.js";

const Interview = () => {
  const [role, setRole] = useState("Software Engineer");
  const [transcript, setTranscript] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const response = await submitInterview({
      user_id: "demo-user",
      role,
      transcript
    });
    setResult(response);
  };

  return (
    <section>
      <h1>Interview Mode</h1>
      <label>
        Role
        <input
          value={role}
          onChange={(event) => setRole(event.target.value)}
          style={{ marginLeft: "8px" }}
        />
      </label>
      <div style={{ marginTop: "12px" }}>
        <textarea
          rows={4}
          style={{ width: "100%" }}
          placeholder="Paste transcript here"
          value={transcript}
          onChange={(event) => setTranscript(event.target.value)}
        />
      </div>
      <button onClick={handleSubmit} style={{ marginTop: "12px" }}>
        Submit Interview
      </button>
      {result && (
        <div style={{ marginTop: "16px" }}>
          <h2>Overall Score: {result.overall_score}</h2>
          <pre>{JSON.stringify(result.category_scores, null, 2)}</pre>
        </div>
      )}
    </section>
  );
};

export default Interview;
