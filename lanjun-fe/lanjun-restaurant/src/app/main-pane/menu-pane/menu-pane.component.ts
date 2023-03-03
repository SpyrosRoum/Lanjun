import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { CartService } from 'src/app/cart.service';
import { Category } from 'src/app/category.model';
import { ItemService } from 'src/app/item.service';

@Component({
    selector: 'app-menu-pane',
    templateUrl: './menu-pane.component.html',
    styleUrls: ['./menu-pane.component.css']
})
export class MenuPaneComponent implements OnInit, OnDestroy {
    public categories: Category[];
    private subscription: Subscription;
    public count: number;

    constructor(private itemService: ItemService, private cartService: CartService) {
        this.categories = new Array();
        this.count = 0;
        this.subscription = ItemService.categoriesSubject.subscribe(c => {
            this.categories = c;
        })
    }

    ngOnDestroy(): void {
        this.subscription.unsubscribe();
    }

    ngOnInit(): void {
        this.itemService.getAllCategories();
    }

    getCategories(): Category[]{
        return this.categories;
    }

    getCountOfItem(id: string): number{
        return this.cartService.getCountByItemId(id);
    }
}