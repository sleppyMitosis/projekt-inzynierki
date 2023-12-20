<script setup lang="ts">
import { ref } from "vue";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import userService from "@/services/user/userService";
import { useRouter } from "vue-router";
import { Route } from "@/router/route";

const username = ref("");
const password = ref("");
const firstName = ref("");
const lastName = ref("");
const email = ref("");
const phoneNumber = ref("");
const vetPhoneNumber = ref("");
const router = useRouter();

const registerUser = async () => {
  try {
    const response = await userService.registerUser({
      username: username.value,
      password: password.value,
      first_name: firstName.value,
      last_name: lastName.value,
      email: email.value,
      phone_number: phoneNumber.value,
      vet_phone_number: vetPhoneNumber.value,
    });
    if (response.status === 200 || response.status === 201) {
      router.push({ name: "loginForm" });
    }
  } catch (error) {
    console.error("Registration failed:", error);
  }
};
</script>
<template>
  <div
    class="flex justify-center items-center h-screen w-screen bg-gradient-to-r from-indigo-300 via-sky-300 to-emerald-200"
  >
    <div
      class="w-[700px] h-[7000px] bg-white/[0.4] rounded-xl flex flex-col items-center justify-center"
    >
      <div class="text-4xl text-center pb-5">Rejestracja</div>
      <div class="flex flex-col gap-2 items-center">
        <div class="w-96 rounded">
          <v-text-field
            v-model="username"
            label="Login"
            variant="outlined"
            bg-color="#fff"
          ></v-text-field>
        </div>
        <div class="w-96 rounded">
          <v-text-field
            v-model="password"
            label="Hasło"
            variant="outlined"
            bg-color="#fff"
          ></v-text-field>
        </div>
        <div class="w-96 rounded">
          <v-text-field
            v-model="firstName"
            label="Imię"
            variant="outlined"
            bg-color="#fff"
          ></v-text-field>
        </div>
        <div class="w-96 rounded">
          <v-text-field
            v-model="lastName"
            label="Nazwisko"
            variant="outlined"
            bg-color="#fff"
          ></v-text-field>
        </div>
        <div class="w-96 rounded">
          <v-text-field
            v-model="email"
            label="E-mail"
            variant="outlined"
            bg-color="#fff"
          ></v-text-field>
        </div>
        <div class="w-96 rounded">
          <v-text-field
            v-model="phoneNumber"
            label="Numer telefonu"
            variant="outlined"
            bg-color="#fff"
          ></v-text-field>
        </div>
        <div class="w-96 rounded">
          <v-text-field
            v-model="vetPhoneNumber"
            label="Numer telefonu weterynarza"
            variant="outlined"
            bg-color="#fff"
          ></v-text-field>
        </div>
      </div>

      <div
        class="rounded flex items-center justify-center text-cornflowerblue pt-4"
      >
        <ButtonItem @click="registerUser">Zarejestruj się</ButtonItem>
      </div>
    </div>
  </div>
</template>
