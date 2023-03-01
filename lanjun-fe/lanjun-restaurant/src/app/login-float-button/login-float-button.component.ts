import { Component, OnInit } from '@angular/core';
import { FormBuilder, NgForm } from '@angular/forms';
import { Subscription } from 'rxjs';
import { AuthService } from '../auth.service';


@Component({
  selector: 'app-login-float-button',
  templateUrl: './login-float-button.component.html',
  styleUrls: ['./login-float-button.component.css'],
  providers: [FormBuilder, AuthService]
})
export class LoginFloatButtonComponent implements OnInit {
  public logged: boolean;
  public toggle: boolean;
  private subscription: Subscription;

  constructor(private fb: FormBuilder, private authService: AuthService) {
    this.logged = false;
    this.toggle = false;
    this.subscription = AuthService.loggedinSubject.subscribe(l => {
      this.logged = l;
    })
  }

  ngOnInit(): void {
  }

  toggleDiv() {
    this.toggle = !this.toggle;
  }

  login(form: NgForm) {
    console.log(form.value);
    if (form.value.email && form.value.password) {
      this.authService.login(form.value.email, form.value.password);
    }
    form.resetForm();//works
    return false;
  }

  signup(form: NgForm) {
    if(form.value.email && form.value.name && form.value.password && (form.value.password === form.value.c_password) && form.value.phone && form.value.address){
      this.authService.signup(form.value.email, form.value.name, form.value.password, form.value.phone, form.value.address, form.value.floor, form.value.bell);
    }
    
    console.log(form.value);
  }
}
