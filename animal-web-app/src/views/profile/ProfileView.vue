<script setup lang="ts">
import { onMounted } from "vue";
import EditPassword from "@/views/profile/EditPassword.vue";
import { useUserStore } from "@/stores/profileStore";
import { storeToRefs } from "pinia";
import ButtonItem from "@/components/button-item/ButtonItem.vue";

const userStore = useUserStore();
const {
  isEditPasswordOpen,
  username,
  email,
  first_name,
  last_name,
  phone_number,
  vet_phone_number,
} = storeToRefs(userStore);

onMounted(() => {
  if (!userStore.userIsLoaded) {
    userStore.getUserFromApi();
  }
});
</script>

<template>
  <div class="bg-[#F1F1F1] flex h-full w-full p-10">
    <div
      class="p-4 bg-sky-100 border rounded-2xl flex flex-col w-[550px] shadow-xl"
    >
      <p class="text-[32px] text-black font-bold opacity-100">Moje konto</p>
      <div class="text-black mt-4">
        <p class="font-bold text-base py-2">
          Imię i nazwisko: {{ first_name }} {{ last_name }}
        </p>
        <p class="font-bold text-base py-2">Adres email: {{ email }}</p>
        <p class="font-bold text-base py-2">Login: {{ username }}</p>
        <p class="font-bold text-base py-2">
          Numer telefonu: {{ phone_number }}
        </p>
        <p class="font-bold text-base py-2">
          Numer telefonu do weterynarza: {{ vet_phone_number }}
        </p>
        <div class="flex flex-row py-10">
          <div class="justify-center items-center align-center">
            <ButtonItem
              size="medium"
              type="secondary"
              class="bg-white"
              @click="isEditPasswordOpen = true"
              >Edytuj profil</ButtonItem
            >
          </div>
          <v-expand-x-transition>
            <div
              v-if="isEditPasswordOpen"
              class="absolute top-0 right-0 z-10 w-[500px] h-screen"
            >
              <EditPassword />
            </div>
          </v-expand-x-transition>
        </div>
      </div>
    </div>
  </div>
</template>
