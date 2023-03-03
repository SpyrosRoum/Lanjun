import { Component, Input, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import { Order } from 'src/app/order.model';

@Component({
  selector: 'app-order-table',
  templateUrl: './order-table.component.html',
  styleUrls: ['./order-table.component.css']
})
export class OrderTableComponent implements OnInit {
  @Input() orders: Order[];
  constructor(private api: ApiService) {
    this.orders = new Array();
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
    this.api.deleteItem(id).subscribe((d) => {
      console.log(d);
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
