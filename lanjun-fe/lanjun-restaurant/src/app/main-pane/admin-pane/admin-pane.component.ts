import { Component, OnInit } from '@angular/core';
import { ItemService } from 'src/app/item.service';

@Component({
  selector: 'app-admin-pane',
  templateUrl: './admin-pane.component.html',
  styleUrls: ['./admin-pane.component.css']
})
export class AdminPaneComponent implements OnInit {
  public count: number;
  constructor(private itemService: ItemService) {
    this.count = 0;
  }

  ngOnInit(): void {
    this.itemService.getAllItems();
  }
}
