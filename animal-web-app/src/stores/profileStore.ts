import { defineStore, storeToRefs } from "pinia";
import { ref, watch, computed } from "vue";
import { Route } from "@/router/route";
import router from "@/router";
import userService from "@/services/user/userService";
import auth from "@/services/auth/auth";
import type { UserEditData } from "@/services/user/user.model";

export const useUserStore = defineStore("user", () => {
  const isEditPasswordOpen = ref<boolean>(false);

  const id = ref();
  const username = ref("");
  const email = ref("");
  const first_name = ref("");
  const last_name = ref("");
  const phone_number = ref("");
  const vet_phone_number = ref("");
  const userIsLoaded = ref(false);
  const isUserLoggedIn = computed(() => userIsLoaded.value && id.value != null);

  async function getUserFromApi() {
    try {
      const response = await userService.getUserDetail();
      if (response.status === 200) {
        userIsLoaded.value = true;
        const userData = response.data;
        id.value = userData.id;
        username.value = userData.username;
        email.value = userData.email;
        first_name.value = userData.first_name;
        last_name.value = userData.last_name;
        phone_number.value = userData.phone_number;
        vet_phone_number.value = userData.vet_phone_number;
      }
    } catch (error) {
      console.error("Failed to fetch user:", error);
      router.push(Route.loginForm.path);
    }
  }

  async function editProfile(updatedProfile: UserEditData) {
    const response = await userService.updateProfile(updatedProfile);
    first_name.value = updatedProfile.first_name;
    last_name.value = updatedProfile.last_name;
    phone_number.value = updatedProfile.phone_number;
    vet_phone_number.value = updatedProfile.vet_phone_number;
    email.value = updatedProfile.email;

    return response;
  }

  function clearUserData() {
    userIsLoaded.value = false;
    id.value = null;
    username.value = "";
    email.value = "";
    first_name.value = "";
    last_name.value = "";
    phone_number.value = "";
    vet_phone_number.value = "";
  }

  return {
    isEditPasswordOpen,
    id,
    username,
    email,
    first_name,
    last_name,
    phone_number,
    vet_phone_number,
    userIsLoaded,
    getUserFromApi,
    clearUserData,
    isUserLoggedIn,
    editProfile,
  };
});
