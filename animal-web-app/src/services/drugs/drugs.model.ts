import type { AxiosResponse } from "axios";
import { Animal } from "@/services/animals/animals.model";

export interface Medication {
  id: number;
  animal?: Animal | null;
  name: string;
  start_date: string;
  end_date: string;
  dosage_count: number;
}

export interface CreateMedication {
  id?: number;
  animal_id?: number | undefined;
  name: string;
  start_date: string;
  end_date: string;
  dosage_count: number;
}

export type DrugsResponse = AxiosResponse<Medication[]>;
