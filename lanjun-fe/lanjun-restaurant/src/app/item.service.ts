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
        let str = JSON.stringify(jsonfile);
        this.categories = new Array();//JSON.parse(str).categories;
        this.api.getItems().subscribe(
            data => {
                console.log(data);
                // this.categories = JSON.parse(data);
                this.categories = JSON.parse(str).categories;
                this.categories.forEach(category => {
                    category.items.forEach(item =>{
                        item.category = category.name;
                    })
                    this.items.push(...category.items);
                })
            },
            err => {
                console.log(err);
            }
        );

    }

    getAllCategories() {
        ItemService.categoriesSubject.next(this.categories);
    }

    getAllItems() {
        ItemService.itemSubject.next(this.items);
    }

    getItemById(id: string): Item {
        return this.items.filter(i => i.id === id)[0];
    }
}