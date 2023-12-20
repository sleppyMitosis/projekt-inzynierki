<script lang="ts">
import { defineComponent, ref } from "vue";
import auth from "@/services/auth/auth"; // Ensure this path is correct
import { useRouter } from "vue-router";
import { Route } from "@/router/route";
import ButtonItem from "@/components/button-item/ButtonItem.vue"; // Import ButtonItem component

export default defineComponent({
  components: { ButtonItem },
  setup() {
    const login = ref("");
    const password = ref("");
    const router = useRouter();

    const sendLoginRequest = async () => {
      try {
        await auth.login({ username: login.value, password: password.value });
        router.push(Route.dashboard.path);
      } catch (error) {
        console.error("Login failed:", error);
      }
    };

    const navigateToNewUser = () => {
      router.push({ name: "newUser" });
    };

    return { login, password, sendLoginRequest, navigateToNewUser };
  },
});
</script>
<template>
  <div
    class="flex justify-center items-center h-screen w-screen bg-gradient-to-r from-indigo-300 via-sky-300 to-emerald-200"
  >
    <div
      class="w-[550px] h-[500px] bg-white/[0.4] rounded-xl flex flex-col items-center justify-center"
    >
      <div class="text-4xl text-center">Zaloguj się</div>
      <div class="flex flex-col gap-2 pt-8 items-center">
        <div class="w-80 h-10 rounded">
          <v-text-field
            v-model="login"
            label="Adres email lub login"
            variant="outlined"
            bg-color="#fff"
          ></v-text-field>
        </div>
        <div class="w-80 rounded pt-5">
          <v-text-field
            v-model="password"
            label="Hasło"
            variant="outlined"
            bg-color="#fff"
          ></v-text-field>
        </div>
      </div>
      <p
        class="flex [text-decoration:underline] font-semibold justify-center pl-36 py-4 cursor-pointer"
        @click="navigateToNewUser"
      >
        Nie masz konta?
      </p>
      <div
        class="rounded flex items-center justify-center text-cornflowerblue pt-4"
      >
        <ButtonItem @click="sendLoginRequest">Zaloguj</ButtonItem>
      </div>
    </div>
  </div>
</template>
