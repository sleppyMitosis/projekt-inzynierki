import axios from "axios";

const getToken = () => {
  const token = localStorage.getItem("token");
  console.log("Retrieved token:", token); // For debugging; remove later
  return token;
};

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:8000/",
  headers: {
    "Content-Type": "application/json",
    ...(getToken() ? { Authorization: `Token ${getToken()}` } : {}),
  },
  withCredentials: true,
});

export default apiClient;
