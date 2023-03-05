export class CartItemSimple {
    item_id: string;
    count: number;

    constructor(item_id: string, count: number) {
        this.item_id = item_id;
        this.count = count;
    }
}