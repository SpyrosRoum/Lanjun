import { Component, Input, OnInit } from '@angular/core';
import { Item } from 'src/app/item.model';

@Component({
  selector: 'app-item-table',
  templateUrl: './item-table.component.html',
  styleUrls: ['./item-table.component.css']
})
export class ItemTableComponent implements OnInit {
  @Input() items: Item[];
  constructor() {
    this.items = new Array();
  }

  ngOnInit(): void {
  }

  edit(id: number, type: string) {
    //enable inputs
    let els: HTMLCollectionOf<HTMLInputElement> = document.getElementsByTagName("input");

    for (let i = 0; i < els.length; i++) {

      if (els[i].id === type + id) {
        els[i].disabled = false;
        if (els[i].name === 'hide') {
          els[i].hidden = false;
        }
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

  save(id: number, type: string) {
    //backend logic

    //enable inputs
    let els: HTMLCollectionOf<HTMLInputElement> = document.getElementsByTagName("input");

    for (let i = 0; i < els.length; i++) {

      if (els[i].id === type + id) {
        els[i].disabled = true;
        if (els[i].name === 'hide') {
          els[i].hidden = true;
        }
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
  }

  deleteCheck(id: number, type: string) {
    //show r u sure
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

  deleteItem(id: number, type: string) {
    //backend logic
    console.log("deleted");

    this.showBin(id, type);
  }

  showBin(id: number, type: string) {
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
    let n, i, d, p;
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
      p = priceE.value;
    }

    console.log(n + " " + i + " " + d + " " + p);

  }

}
