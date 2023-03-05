import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { ApiService } from './api.service';
import { Order } from './order.model';

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  private orders: Order[];
  static orderSubject: Subject<Order[]> = new Subject();

  constructor(private api: ApiService) {
    this.orders = new Array();
    this.setOrders();
  }

  public setOrders() {
    this.api.getOrders().subscribe(
      data => {
        console.log("set orders");
        console.log(data);
        this.orders = data.orders;
        OrderService.orderSubject.next(this.orders);
      },
      err => {
        console.log(err);
      })
  }

  public getAllOrders() {
    OrderService.orderSubject.next(this.orders);
  }
}
