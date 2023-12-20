import apiClient from "@/services/apiClient";
import type {
  UserResponse,
  UserEditData,
  UserRegistrationData,
} from "@/services/user/user.model";

export default {
  getUserDetail(): Promise<UserResponse> {
    return apiClient.get("/user/api/user-detail");
  },

  async updateProfile(updatedProfile: UserEditData) {
    const response = await apiClient.put("user/api/edit-profile/", {
      ...updatedProfile,
    });
    return response.data;
  },

  async registerUser(userData: UserRegistrationData) {
    return apiClient.post("/user/api/register/", userData);
  },
};
