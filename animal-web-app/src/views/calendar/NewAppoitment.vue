<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import DatePicker from "@vuepic/vue-datepicker";
import { useAppointmentStore } from "@/stores/appointmentsStore";
import { storeToRefs } from "pinia";
import { ref, watch } from "vue";

const appointmentStore = useAppointmentStore();
appointmentStore.getAppointments();
appointmentStore.getAnimals();

const {
  appointments,
  selectedAppointment,
  isNewAppointmentOpen,
  animalOptions,
} = storeToRefs(appointmentStore);

const date = ref("");
const name = ref("");
const animal_id = ref(selectedAppointment.value?.animal?.id);
const description = ref("");
const appointment_time = ref("");
const appointment_date = ref(selectedAppointment.value?.appointment_date || "");

// const newAppointment = ref({
//   date: "", // This will hold the combined date and time
//   name: "",
//   animal: undefined,
//   description: "",
//   appointment_date: "",
//   appointment_time: "",
// });

function formatTime(timeString: string): string {
  if (!timeString) return "";
  const time = new Date(`1970-01-01T${timeString}`);

  if (isNaN(time.getTime())) {
    return "";
  }

  const hours = time.getHours().toString().padStart(2, "0");
  const minutes = time.getMinutes().toString().padStart(2, "0");

  return `${hours}:${minutes}`;
}

const saveAppointment = async () => {
  const appointmentData = {
    name: name.value,
    animal_id: animal_id.value,
    description: description.value,
    appointment_time: formatTime(appointment_time.value),
    appointment_date: formatDate(appointment_date.value),
  };

  await appointmentStore.postAppointment(appointmentData);
  isNewAppointmentOpen.value = false;
};

function formatDate(dateString: string | null): string {
  if (!dateString) return "";
  const date = new Date(dateString);
  if (isNaN(date.getTime())) {
    return "";
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
        @click="isNewAppointmentOpen = false"
      />
    </div>
    <div
      class="relative bg-color-white w-full flex flex-col items-start justify-start px-6 box-border gap-[8px] text-left text-sm text-colors-text-field-standard font-body-standard-regular"
    >
      <div class="flex gap-6 w-full pb-4">
        <p class="text-[28px]">Dodaj wizytę</p>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start pb-5"
      >
        <DatePicker
          :enable-time-picker="false"
          placeholder="Data wizyty"
          format="yyyy-MM-dd"
          locale="pl"
          v-model="appointment_date"
        ></DatePicker>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start pb-5"
      >
        <input
          type="time"
          v-model="appointment_time"
          class="border-2 border-gray-900 border rounded px-3 py-2 w-full"
          placeholder="Godzina wizyty"
        />
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          v-model="name"
          variant="outlined"
          density="compact"
          label="Nazwa wizyty"
          placeholder="Nazwa wizyty"
        ></v-text-field>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start pb-5"
      >
        <v-select
          variant="outlined"
          bg-color="#fff"
          :items="animalOptions"
          item-title="label"
          item-value="value"
          density="compact"
          label="Zwierzę"
          hide-details
          v-model="animal_id"
          clearable
        ></v-select>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          v-model="description"
          variant="outlined"
          density="compact"
          label="Opis wizyty (opcjonlanie)"
          placeholder="Opis wizyty (opcjonlanie)"
        ></v-text-field>
      </div>
    </div>
    <div class="flex justify-center flex-col w-full pt-6">
      <ButtonItem @click="saveAppointment">Dodaj wizytę</ButtonItem>
      <ButtonItem type="tertiary" @click="isNewAppointmentOpen = false"
        >Anuluj</ButtonItem
      >
    </div>
  </div>
</template>
