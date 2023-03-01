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

    constructor(private api:ApiService) {
        let str = JSON.stringify(jsonfile);
        this.categories = JSON.parse(str).categories;
        this.api.getItems().subscribe(
            data => {
                console.log(data);

            },
            err => {
                console.log(err);
            }
        );
        this.items = new Array();
        this.categories.forEach(category => {
            this.items.push(...category.items);
        })
    }

    getAllCategories() {
        ItemService.categoriesSubject.next(this.categories);
    }

    getAllItems() {
        ItemService.itemSubject.next(this.items);
    }

    getItemById(id: number): Item {
        return this.items.filter(i => i.id === id)[0];
    }
}