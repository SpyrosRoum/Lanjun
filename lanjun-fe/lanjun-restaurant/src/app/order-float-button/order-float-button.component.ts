import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { CartService } from '../cart.service';
import { SwapperService } from '../swapper.service';

@Component({
  selector: 'app-order-float-button',
  templateUrl: './order-float-button.component.html',
  styleUrls: ['./order-float-button.component.css']
})
export class OrderFloatButtonComponent implements OnInit, OnDestroy {
  public count: number;
  private subscription: Subscription;
  constructor(private swapperService: SwapperService, private cartService: CartService) { 
    this.count = 0;

    this.subscription = CartService.cartItemCountSubject.subscribe(cic=>{
      this.count = cic;
    })
  }
  ngOnDestroy(): void {
    this.subscription.unsubscribe()
  }

  ngOnInit(): void {
  }

  swapper(panel: string): void {
    this.swapperService.setPanel(panel);
  }
}
