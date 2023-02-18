import { Component, OnInit } from '@angular/core';
import { CartItem } from 'src/app/cart-item.model';
import { CartService } from 'src/app/cart.service';
import { ItemService } from 'src/app/item.service';
import { SwapperService } from 'src/app/swapper.service';

@Component({
  selector: 'app-delivery-pane',
  templateUrl: './delivery-pane.component.html',
  styleUrls: ['./delivery-pane.component.css']
})
export class DeliveryPaneComponent implements OnInit {
  public cartItems: CartItem[];
  public sum: number = 0;
  public reservation: boolean;
  
  constructor(private cartService: CartService, private itemService: ItemService, private swapperService: SwapperService) {
    this.cartItems = cartService.getCartItems();
    this.sum = cartService.getPriceSum();
    this.reservation = false;

    CartService.cartItemListSubject.subscribe(im => {
      this.sum = 0;
      this.cartItems = new Array();

      for (let id of im.keys()) {
        let c = im.get(id);

        if (c != undefined) {
          let ci = new CartItem(itemService.getItemById(id), c);

          this.cartItems.push(ci);
          this.sum += ci.item.price;
        }
      }
    })
  }

  ngOnInit(): void { }

  swapper(panel: string): void {
    this.swapperService.setPanel(panel);
  }

  buy(){
    //TODO: to be discussed 
  }

  toggleReservation(){    
    this.reservation = !this.reservation;
  }
}
