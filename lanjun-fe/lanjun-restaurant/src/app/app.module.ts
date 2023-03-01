import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { MainPaneComponent } from './main-pane/main-pane.component';
import { OrderFloatButtonComponent } from './order-float-button/order-float-button.component';
import { SideBarComponent } from './side-bar/side-bar.component';
import { MenuPaneComponent } from './main-pane/menu-pane/menu-pane.component';
import { LoginFloatButtonComponent } from './login-float-button/login-float-button.component';
import { AddToCartComponent } from './main-pane/menu-pane/add-to-cart/add-to-cart.component';
import { DeliveryPaneComponent } from './main-pane/delivery-pane/delivery-pane.component';
import { ItemComponent } from './main-pane/menu-pane/item/item.component';
import { ReservationPaneComponent } from './main-pane/reservation-pane/reservation-pane.component';
import { AboutPaneComponent } from './main-pane/about-pane/about-pane.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AdminPaneComponent } from './main-pane/admin-pane/admin-pane.component';
import { ItemTableComponent } from './main-pane/admin-pane/item-table/item-table.component';

@NgModule({
  declarations: [
    AppComponent,
    MainPaneComponent,
    OrderFloatButtonComponent,
    SideBarComponent,
    MenuPaneComponent,
    LoginFloatButtonComponent,
    AddToCartComponent,
    DeliveryPaneComponent,
    ItemComponent,
    ReservationPaneComponent,
    AboutPaneComponent,
    AdminPaneComponent,
    ItemTableComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
