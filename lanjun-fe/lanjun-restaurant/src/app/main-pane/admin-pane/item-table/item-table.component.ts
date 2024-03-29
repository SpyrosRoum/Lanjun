import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { ApiService } from 'src/app/api.service';
import { Item } from 'src/app/item.model';
import { ItemService } from 'src/app/item.service';

@Component({
  selector: 'app-item-table',
  templateUrl: './item-table.component.html',
  styleUrls: ['./item-table.component.css']
})
export class ItemTableComponent implements OnInit {
  public items: Item[];
  private name: string;
  private img: string;
  private description: string;
  private price: number;
  private category: string;

  private itemSubscription: Subscription;

  constructor(private api: ApiService, private itemService: ItemService) {
    this.items = new Array();
    this.name = "";
    this.img = "";
    this.description = "";
    this.price = 0;
    this.category = "";

    this.itemSubscription = ItemService.itemSubject.subscribe(c => {
      this.items = c;
    })
  }

  reset() {
    this.name = "";
    this.img = "";
    this.description = "";
    this.price = 0;
    this.category = "";
  }

  ngOnInit(): void {
  }

  edit(id: string, type: string) {
    //enable inputs
    let els: HTMLCollectionOf<HTMLInputElement> = document.getElementsByTagName("input");

    //save old values
    this.name = "";
    this.img = "";
    this.description = "";
    this.price = 0;
    this.category = "";

    for (let i = 0; i < els.length; i++) {
      let cleanElId: string = els[i].id.substring(els[i].id.indexOf("_") + 1);
      if (cleanElId != type + id) continue;

      els[i].disabled = false;
      if (els[i].name === 'hide') {
        els[i].hidden = false;
      }

      switch (els[i].id.substring(0, els[i].id.indexOf("_"))) {
        case "name":
          this.name = els[i].value;
          break;
        case "img":
          this.img = els[i].value;
          break;
        case "description":
          this.description = els[i].value;
          break;
        case "price":
          this.price = +els[i].value;
          break;
        case "category":
          this.category = els[i].value;
          break;
      }

    }
    //hide image
    let img = document.getElementById("img_" + type + id);
    if (img) {
      img.hidden = true;
    }

    //hide edit and show save
    let edit = document.getElementById("edit_" + type + id);
    if (edit) {
      edit.hidden = true;
    }

    let save = document.getElementById("save_" + type + id);
    if (save) {
      save.hidden = false;
    }
  }

  save(id: string, type: string) {
    //enable inputs
    let els: HTMLCollectionOf<HTMLInputElement> = document.getElementsByTagName("input");

    let changes: boolean = false;

    for (let i = 0; i < els.length; i++) {
      let cleanElId: string = els[i].id.substring(els[i].id.indexOf("_") + 1);
      if (cleanElId != type + id) continue

      els[i].disabled = true;
      if (els[i].name === 'hide') {
        els[i].hidden = true;
      }

      switch (els[i].id.substring(0, els[i].id.indexOf("_"))) {
        case "name":
          changes = changes || this.name != els[i].value;
          if (this.name != els[i].value)
            this.name = els[i].value;
          break;
        case "img":
          changes = changes || this.img != els[i].value;
          if (this.img != els[i].value)
            this.img = els[i].value;
          break;
        case "description":
          changes = changes || this.description != els[i].value;
          if (this.description != els[i].value)
            this.description = els[i].value;
          break;
        case "price":
          changes = changes || this.price != +els[i].value;
          if (this.price != +els[i].value)
            this.price = +els[i].value;
          break;
        case "category":
          changes = changes || this.category != els[i].value;
          if (this.category != els[i].value)
            this.category = els[i].value;
          break;
      }
    }
    //hide image
    let img = document.getElementById("img_" + type + id);
    if (img) {
      img.hidden = false;
    }

    //hide save  and show edit
    let edit = document.getElementById("edit_" + type + id);
    if (edit) {
      edit.hidden = false;
    }

    let save = document.getElementById("save_" + type + id);
    if (save) {
      save.hidden = true;
    }

    if (changes) {
      console.log("changes");
      this.api.updateItem(id, this.name, this.img, this.description, this.price, this.category).subscribe(u => {
        this.itemService.setItems();
      });
    }
    //reset the values to empty
    this.reset();
  }

  deleteCheck(id: string, type: string) {

    let bin = document.getElementById("bin_" + type + id);
    if (bin) {
      bin.hidden = true;
    }

    let yes = document.getElementById("yes_" + type + id);
    if (yes) {
      yes.hidden = false;
    }

    let no = document.getElementById("no_" + type + id);
    if (no) {
      no.hidden = false;
    }
  }

  deleteItem(id: string, type: string) {
    this.api.deleteItem(id).subscribe((d) => {
      this.itemService.setItems();
    });

    this.showBin(id, type);
  }

  showBin(id: string, type: string) {
    let bin = document.getElementById("bin_" + type + id);
    if (bin) {
      bin.hidden = false;
    }

    let yes = document.getElementById("yes_" + type + id);
    if (yes) {
      yes.hidden = true;
    }

    let no = document.getElementById("no_" + type + id);
    if (no) {
      no.hidden = true;
    }

  }

  newItem() {
    let nameE = document.getElementById("new_item_name") as HTMLInputElement;
    let imageE = document.getElementById("new_item_image") as HTMLInputElement;
    let descriptionE = document.getElementById("new_item_description") as HTMLInputElement;
    let priceE = document.getElementById("new_item_price") as HTMLInputElement;
    let categoryE = document.getElementById("new_item_category") as HTMLInputElement;
    let n, i, d, p, c;

    if (nameE) {
      n = nameE.value;
    }
    if (imageE) {
      i = imageE.value;
    }
    if (descriptionE) {
      d = descriptionE.value;
    }
    if (priceE) {
      p = +priceE.value;
    }

    if (categoryE) {
      c = categoryE.value;
    }

    this.api.addItem(n, i, d, p, c).subscribe((t) => {
      this.itemService.setItems();
    });

    nameE.value = "";
    imageE.value = "";
    descriptionE.value = "";
    priceE.value = "";
    categoryE.value = "";

  }
}
