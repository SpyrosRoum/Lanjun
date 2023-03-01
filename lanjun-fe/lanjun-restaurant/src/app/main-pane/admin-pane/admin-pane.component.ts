import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { Category } from 'src/app/category.model';
import { Item } from 'src/app/item.model';
import { ItemService } from 'src/app/item.service';

@Component({
  selector: 'app-admin-pane',
  templateUrl: './admin-pane.component.html',
  styleUrls: ['./admin-pane.component.css']
})
export class AdminPaneComponent implements OnInit, OnDestroy {
  public items: Item[];
  private itemSubscription: Subscription;

  public count: number;
  constructor(private itemService: ItemService) {
    this.items = new Array();
    this.count = 0;
    this.itemSubscription = ItemService.itemSubject.subscribe(c => {
      this.items = c;
    })
  }

  ngOnInit(): void {
    this.itemService.getAllItems();
  }

  ngOnDestroy(): void {
    this.itemSubscription.unsubscribe();
  } 

}
