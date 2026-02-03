import React, { useEffect, useState } from "react";
import { fetchDashboard } from "../services/api.js";

const Dashboard = () => {
  const [profile, setProfile] = useState(null);
  const [history, setHistory] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchDashboard("demo-user")
      .then((data) => {
        setProfile(data.profile);
        setHistory(data.history);
      })
      .catch(() => setError("Unable to load dashboard"));
  }, []);

  return (
    <section>
      <h1>Dashboard</h1>
      {error && <p>{error}</p>}
      {profile ? (
        <div>
          <h2>Profile</h2>
          <p>Name: {profile.name}</p>
          <p>Phone: {profile.phone}</p>
          <p>Email: {profile.email}</p>
        </div>
      ) : (
        <p>Loading profile...</p>
      )}
      <div style={{ marginTop: "16px" }}>
        <h2>Interview History</h2>
        {history.length === 0 ? (
          <p>No interviews yet.</p>
        ) : (
          <ul>
            {history.map((item) => (
              <li key={item.id}>
                {item.role} - Score: {item.overall_score}
              </li>
            ))}
          </ul>
        )}
      </div>
    </section>
  );
};

export default Dashboard;
