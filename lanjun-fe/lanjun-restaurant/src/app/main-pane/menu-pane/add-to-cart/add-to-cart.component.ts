import { Component, Input, OnInit } from '@angular/core';
import { CartService } from 'src/app/cart.service';

@Component({
  selector: 'app-add-to-cart',
  templateUrl: './add-to-cart.component.html',
  styleUrls: ['./add-to-cart.component.css']
})
export class AddToCartComponent implements OnInit {

  @Input() itemId: number;
  @Input() count: number;
  @Input() delivery: boolean;

  constructor(private cartService: CartService) {
    this.itemId = -1;
    this.count = 0;
    this.delivery = false;
  }

  ngOnInit(): void {
  }

  add() {
    if (this.count < 9 && !this.delivery) {
      this.count++;
      this.cartService.addItem(this.itemId, this.count);
    }
  }

  remove() {
    if (this.count > 0) {
      this.count--;
      this.cartService.updateItem(this.itemId, this.count);
    }
  }
}
