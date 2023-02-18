import { Item } from "./item.model";

export class CartItem {
    item: Item;
    count: number;

    constructor(item: Item, count: number) {
        this.item = item;
        this.count = count;
    }
}