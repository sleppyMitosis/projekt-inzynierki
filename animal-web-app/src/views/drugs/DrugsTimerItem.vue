<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { Medication } from "@/services/drugs/drugs.model";
import { useDrugsStore } from "@/stores/drugsStore";
import { storeToRefs } from "pinia";
import { onMounted, ref, computed, onUnmounted } from "vue";

const props = defineProps<{ drug: Medication }>();
console.log(props.drug);
const drugsStore = useDrugsStore();

const { drugs, selectedDrug, isEditDrugOpen } = storeToRefs(drugsStore);

const onClick = () => {
  isEditDrugOpen.value = true;
  selectedDrug.value = props.drug;
};

const decrementDosage = () => {
  selectedDrug.value = props.drug;
  drugsStore.decrementDrugDosage(props.drug.id);
};
</script>

<template>
  <div
    class="p-4 bg-sky-100 border rounded-2xl flex flex-col w-[400px] shadow-xl hover:scale-105"
  >
    <div class="text-black mt-4 flex flex-col justify-center items-center">
      <div class="flex flex-row">
        <p class="font-bold text-semibold pt-2.5 text-center px-2">Lek:</p>
        <p class="font-bold text-lg py-2 text-sky-900 py-2 text-center">
          {{ drug?.name }}
        </p>
      </div>
      <div class="flex flex-row">
        <p class="font-bold text-semibold pt-2.5 text-center px-2">Zwierzę:</p>
        <p class="font-bold text-lg py-2 text-sky-900 py-2 text-center">
          {{ drug?.animal?.name }}
        </p>
      </div>
      <div class="flex flex-row">
        <p class="font-bold text-semibold pt-2.5 text-center px-2">
          Liczba dawek:
        </p>
        <p class="font-bold text-lg py-2 text-sky-900 py-2 text-center">
          {{ drug?.dosage_count }}
        </p>
      </div>
      <p class="font-bold text-base py-2">
        Lek powinien być podawany w dniach:
      </p>
      <p class="font-bold text-lg py-2 text-sky-900">
        {{ drug.start_date }} - {{ drug.end_date }}
      </p>
      <p class="font-bold text-base py-2"></p>
      <div class="flex flex-row py-10">
        <div class="justify-center items-center align-center"></div>
      </div>
      <div class="flex justify-center align-baseline items-center">
        <ButtonItem size="small" @click="decrementDosage"
          >Podaj dawkę</ButtonItem
        >
        <ButtonItem type="tertiary" @click="onClick">Edytuj lek</ButtonItem>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
