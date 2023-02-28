import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, NgForm, Validators } from '@angular/forms';
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

  // private formLogin: FormGroup;

  constructor(private fb: FormBuilder, private authService: AuthService) {
    this.logged = false;
    this.toggle = false;

    // this.formLogin = this.fb.group({
    //   email: ['', Validators.required],
    //   password: ['', Validators.required]
    // });
  }

  ngOnInit(): void {
  }

  toggleDiv() {
    this.toggle = !this.toggle;
  }

  login(form: NgForm) {
    // const val = this.formLogin.value;
    console.log(form.value);
    // if (val.email && val.password) {
      // this.authService.login(val.email, val.password)
      //   .subscribe(
      //     () => {
      //       console.log("User is logged in");
      //     }
        // );
    // }
    form.resetForm();//works
    return false;
  }

  signup(form: NgForm) {
    console.log(form.value);
  }
}
