import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import * as jsonfile from 'src/assets/data.json';
import { ApiService } from './api.service';
import { Category } from './category.model';
import { Item } from './item.model';

@Injectable({
    providedIn: 'root'
})
export class ItemService {
    private categories: Category[];
    private items: Item[];
    static categoriesSubject: Subject<Category[]> = new Subject();
    static itemSubject: Subject<Item[]> = new Subject();

    constructor(private api: ApiService) {
        this.items = new Array();
        this.categories = new Array();
        this.setItems();
    }

    getAllCategories() {
        ItemService.categoriesSubject.next(this.categories);
    }

    getAllItems() {
        ItemService.itemSubject.next(this.items);
    }

    setItems() {
        this.api.getItems().subscribe(
            data => {
                this.items = new Array();
                this.categories = data.categories;

                this.categories.forEach(category => {
                    category.items.forEach(item => {
                        item.category = category.name;
                    })
                    let split = category.name.split("_");
                    if (split.length > 1)
                        category.name = split[1];
                    this.items.push(...category.items);
                })

                this.getAllItems();
            },
            err => {
                console.log(err);
            }
        );
    }

    getItemById(id: string): Item {
        return this.items.filter(i => i.id === id)[0];
    }
}