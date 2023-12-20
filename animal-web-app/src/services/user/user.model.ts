import type { AxiosResponse } from "axios";

export interface UserData {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  phone_number: string;
  vet_phone_number: string;
}

export interface UserEditData {
  email: string;
  first_name: string;
  last_name: string;
  phone_number: string;
  vet_phone_number: string;
}

export interface UserRegistrationData {
  username: string;
  password: string;
  email: string;
  first_name: string;
  last_name: string;
  phone_number: string;
  vet_phone_number: string;
}

export type UserResponse = AxiosResponse<UserData>;
