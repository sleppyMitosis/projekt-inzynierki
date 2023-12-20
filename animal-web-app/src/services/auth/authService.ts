import apiClient from "@/services/apiClient";
import type { LoginBody } from "@/services/auth/auth.model";
import { Route } from "@/router/route";
import router from "@/router";

const login = async (username: string, password: string) => {
  const response = await apiClient.post("/user/api/login/", {
    username,
    password,
  });
  if (response.data && response.data.token) {
    localStorage.setItem("token", response.data.token);
  }
  return response;
};

const logout = async () => {
  try {
    await apiClient.post("/user/api/logout/");
    localStorage.removeItem("token");
    router.push({ name: "loginForm" });
  } catch (error) {
    console.error("Logout failed:", error);
  }
};

export default {
  login,
  logout,
};
