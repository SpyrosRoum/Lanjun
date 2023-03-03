import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import { AuthService } from 'src/app/auth.service';
import { CartItem } from 'src/app/cart-item.model';
import { CartService } from 'src/app/cart.service';
import { ItemService } from 'src/app/item.service';
import { Reservation } from 'src/app/reservation.model';
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
  public logged: boolean;
  private reservationR: Reservation;

  constructor(private cartService: CartService, private itemService: ItemService,
    private swapperService: SwapperService,
    private api: ApiService) {
    this.cartItems = cartService.getCartItems();
    this.sum = cartService.getPriceSum();
    this.reservation = false;
    this.logged = false;
    this.reservationR = new Reservation();

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
    });

    this.logged = AuthService.loggedin;
    console.log(AuthService.loggedin);
    console.log(AuthService.token);

    AuthService.loggedinSubject.subscribe(l => {
      console.log("Delivery " + l);

      this.logged = l;
    });
  }

  ngOnInit(): void { }

  swapper(panel: string): void {
    this.swapperService.setPanel(panel);
  }

  buy() {
    //TODO: Add posibility of payment with cash
    this.api.order(AuthService.token, this.sum, true, this.cartItems, this.reservationR);
  }

  reserve(res: Reservation) {
    this.reservationR = res;
  }

  toggleReservation() {
    this.reservation = !this.reservation;
  }

  toggleLoginFloatButton() {
    document.getElementById("login-button")?.click();
  }
}
