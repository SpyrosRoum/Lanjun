import { Item } from "./item.model";

export interface Category {
    name: string;
    items: Item[];
}