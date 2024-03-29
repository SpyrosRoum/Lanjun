import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import { AuthService } from 'src/app/auth.service';
import { CartItem } from 'src/app/cart-item.model';
import { CartService } from 'src/app/cart.service';
import { ItemService } from 'src/app/item.service';
import { OrderService } from 'src/app/order.service';
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
    private api: ApiService, private orderService: OrderService) {
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
          this.sum += ci.item.price * c;
        }
      }
    });

    this.logged = AuthService.loggedin;

    AuthService.loggedinSubject.subscribe(l => {
      this.logged = l;
    });
  }

  ngOnInit(): void { }

  swapper(panel: string): void {
    this.swapperService.setPanel(panel);
  }

  buy() {
    this.api.postOrder(AuthService.token, this.sum, true, this.cartItems, this.reservationR).subscribe(o => {
      this.orderService.setOrders();
      this.cartService.clearCart();
      this.swapper('home');
    });
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
