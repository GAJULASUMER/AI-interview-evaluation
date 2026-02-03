import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000/api"
});

export const fetchDashboard = async (userId) => {
  const [profile, history] = await Promise.all([
    api.get(`/dashboard/profile?user_id=${userId}`),
    api.get(`/dashboard/history?user_id=${userId}`)
  ]);
  return { profile: profile.data, history: history.data.items };
};

export const submitInterview = async (payload) => {
  const response = await api.post("/interview/submit", payload);
  return response.data;
};

export const askChatbot = async (prompt) => {
  const response = await api.post("/chatbot/ask", { prompt });
  return response.data.response;
};
