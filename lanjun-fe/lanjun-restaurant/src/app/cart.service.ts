import { Injectable } from "@angular/core";
import { Subject } from "rxjs";
import { CartItem } from "./cart-item.model";
import { ItemService } from "./item.service";

@Injectable({
    providedIn: 'root'
})
export class CartService {
    private cartItemMap: Map<number, number>;
    private cartItemCount: number;

    static cartItemListSubject: Subject<Map<number, number>> = new Subject();
    static cartItemCountSubject: Subject<number> = new Subject();

    constructor(private itemService: ItemService) {
        this.cartItemMap = new Map<number, number>;
        this.cartItemCount = 0;
    }

    addItem(id: number, count: number) {
        this.cartItemMap.set(id, count);
        this.cartItemCount++;

        CartService.cartItemCountSubject.next(this.cartItemCount);
        CartService.cartItemListSubject.next(this.cartItemMap);
    }

    updateItem(id: number, count: number) {
        if (count === 0) {
            this.cartItemMap.delete(id);
        } else {
            this.cartItemMap.set(id, count);
        }

        this.cartItemCount--;
        CartService.cartItemCountSubject.next(this.cartItemCount);
        CartService.cartItemListSubject.next(this.cartItemMap);
    }

    getCartItems() {
        let cartItems: CartItem[] = new Array();
        for (let id of this.cartItemMap.keys()) {
            let c = this.cartItemMap.get(id);

            if (c != undefined) {
                let ci = new CartItem(this.itemService.getItemById(id), c);
                cartItems.push(ci);
            }
        }

        return cartItems;
    }

    getPriceSum(): number {
        let list = this.getCartItems();
        if (list.length > 0) {
            return this.getCartItems().map(ci => ci.item.price * ci.count).reduce((prev, cur) => prev + cur);
        } else {
            return 0;
        }
    }

    getCountByItemId(id: number) {        
        let a = this.getCartItems().filter(i => i.item.id === id); 
        
        if (a.length === 0) {
            return 0;
        } else {
            return a[0].count;
        }

    }
} 