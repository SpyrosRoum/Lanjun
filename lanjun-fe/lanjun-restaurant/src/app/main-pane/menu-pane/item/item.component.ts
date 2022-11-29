import { Component, Input, OnInit } from '@angular/core';
import { Item } from 'src/app/item.model';

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.css']
})
export class ItemComponent implements OnInit {
  @Input() public item: Item;
  @Input() count: number;
  @Input() delivery: boolean;

  constructor() {
    this.item = new Item();
    this.count = 0;
    this.delivery = false;
  }

  ngOnInit(): void {
  }

}
