import { Component, Input, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { ApiService } from 'src/app/api.service';
import { ItemService } from 'src/app/item.service';
import { Order } from 'src/app/order.model';
import { OrderService } from 'src/app/order.service';

@Component({
  selector: 'app-order-table',
  templateUrl: './order-table.component.html',
  styleUrls: ['./order-table.component.css']
})
export class OrderTableComponent implements OnInit {
  public orders: Order[];

  private orderSubscription: Subscription;

  constructor(private api: ApiService, private orderService: OrderService) {
    this.orders = new Array();
    this.orderSubscription = OrderService.orderSubject.subscribe(o => {
      this.orders = o;
    });
  }

  ngOnInit(): void {
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

  deleteOrder(id: string, type: string) {
    this.api.deleteOrder(id).subscribe((d) => {
      this.orderService.setOrders();
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
}
