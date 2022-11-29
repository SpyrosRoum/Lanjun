import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import * as jsonfile from 'src/assets/data.json';
import { Category } from './category.model';
import { Item } from './item.model';

@Injectable({
    providedIn: 'root'
})
export class ItemService {
    private categories: Category[];
    private items: Item[];
    static categoriesSubject: Subject<Category[]> = new Subject();

    constructor() {
        let str = JSON.stringify(jsonfile);
        this.categories = JSON.parse(str).categories;

        this.items = new Array();
        this.categories.forEach(category => {
            this.items.push(...category.items);
        })
    }

    getAllCategories() {
        ItemService.categoriesSubject.next(this.categories);
    }

    getItemById(id: number): Item {
        return this.items.filter(i => i.id === id)[0];
    }
}