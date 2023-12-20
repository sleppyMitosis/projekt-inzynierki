import type { AxiosResponse } from "axios";

export interface SelectOption<T> {
  value: T;
  label: string;
}
