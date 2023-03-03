import { Component, OnInit } from '@angular/core';
import { FormBuilder, NgForm } from '@angular/forms';
import { Subscription } from 'rxjs';
import { AuthService } from '../auth.service';
import { SwapperService } from '../swapper.service';


@Component({
  selector: 'app-login-float-button',
  templateUrl: './login-float-button.component.html',
  styleUrls: ['./login-float-button.component.css'],
  providers: [FormBuilder, AuthService]
})
export class LoginFloatButtonComponent implements OnInit {
  public logged: boolean;
  public toggle: boolean;
  public loginTab: boolean;
  private subscription: Subscription;

  constructor(private fb: FormBuilder, private authService: AuthService, private swapperService: SwapperService) {
    this.logged = false;
    this.toggle = false;
    this.loginTab = true;
    
    this.subscription = AuthService.loggedinSubject.subscribe(l => {
      this.logged = l;
    })
  }

  ngOnInit(): void {
  }

  toggleDiv() {
    this.toggle = !this.toggle;
    this.loginTab = true;
  }

  changeTab(tab: boolean) {
    this.loginTab = tab;
    if (tab) {
      document.getElementById("tab-button-login")?.setAttribute("active", "true");
      document.getElementById("tab-button-signup")?.removeAttribute("active");
    } else {
      document.getElementById("tab-button-signup")?.setAttribute("active", "true");
      document.getElementById("tab-button-login")?.removeAttribute("active");
    }
  }

  login(form: NgForm) {
    if (form.value.email && form.value.password) {
      this.authService.login(form.value.email, form.value.password);
    }
    form.resetForm();//works
    return false;
  }

  signup(form: NgForm) {
    if (form.value.email && form.value.name && form.value.password && (form.value.password === form.value.c_password) && form.value.phone && form.value.address) {
      this.authService.signup(form.value.email, form.value.name, form.value.password, form.value.phone, form.value.address, form.value.floor, form.value.bell);
    }

    form.resetForm();//works
    return false;
  }

  swapper() {
    this.swapperService.setPanel('admin');
  }
}
