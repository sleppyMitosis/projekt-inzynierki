<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { storeToRefs } from "pinia";
import { useAnimalsStore } from "@/stores/animalsStore";
import { ref } from "vue";
import DatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

const animalStore = useAnimalsStore();
const { animals, isNewAnimalOpen, selectedAnimal } = storeToRefs(animalStore);

const name = ref(selectedAnimal.value?.name || "");
const species = ref(selectedAnimal.value?.species || "");
const chip = ref(selectedAnimal.value?.chip_number || "");
const birthday = ref(selectedAnimal.value?.date_of_birth || "");

const addNewanimal = async () => {
  const newAnimal = {
    name: name.value,
    species: species.value,
    chip_number: chip.value,
    date_of_birth: formatDate(birthday.value),
  };
  await animalStore.postAnimal(newAnimal);
  animalStore.getAnimals();
  isNewAnimalOpen.value = false;
};

function formatDate(dateString: string | null): string | null {
  if (!dateString) return null;
  const date = new Date(dateString);

  if (isNaN(date.getTime())) {
    return null;
  }

  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const day = date.getDate().toString().padStart(2, "0");

  return `${year}-${month}-${day}`;
}
</script>

<template>
  <div
    class="overflow-y-auto bg-white w-full h-full flex flex-col px-6 pt-6 pb-6 text-left text-base border-l border-solid border-grey-two"
  >
    <div class="flex justify-end">
      <font-awesome-icon
        :icon="['fas', 'xmark']"
        style="color: #000000"
        size="2xl"
        @click="isNewAnimalOpen = false"
      />
    </div>
    <div
      class="relative bg-color-white w-full flex flex-col items-start justify-start px-6 box-border gap-[8px] text-left text-sm text-colors-text-field-standard font-body-standard-regular"
    >
      <div class="flex gap-6 w-full pb-4">
        <p class="text-[28px]">Dodaj zwierzaka</p>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          variant="outlined"
          density="compact"
          label="Imię"
          placeholder="Imię"
          v-model="name"
        ></v-text-field>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          variant="outlined"
          density="compact"
          label="Gatunek"
          placeholder="Gatunek"
          v-model="species"
        ></v-text-field>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start pb-"
      >
        <DatePicker
          :enable-time-picker="false"
          placeholder="Data Urodzenia"
          :format="'yyyy-MM-dd'"
          locale="pl"
          v-model="birthday"
        ></DatePicker>
      </div>

      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          variant="outlined"
          density="compact"
          label="Numer chipa lub rodowodu"
          placeholder="Numer chipa lub rodowodu"
          v-model="chip"
        ></v-text-field>
      </div>
    </div>
    <div class="flex justify-center flex-col w-full pt-6">
      <ButtonItem @click="addNewanimal">Zapisz zmiany</ButtonItem>
      <ButtonItem type="tertiary" @click="isNewAnimalOpen = false"
        >Anuluj</ButtonItem
      >
    </div>
  </div>
</template>

<style>
.dp__theme_light {
  --dp-border-color: #aaaeb7;
  --dp-border-color-hover: #222226;
  --dp-primary-text-color: #222226;
  --dp-primary-color: #0ea5e9;
}
:root {
  --dp-input-padding: 9px 30px 9px 12px;
}
</style>
