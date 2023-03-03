import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { ApiService } from './api.service';
import { User } from './user.model';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  static user: User;
  static loggedin: boolean;
  static token: string;
  static loggedinSubject: Subject<boolean> = new Subject();

  constructor(private api: ApiService) {
    AuthService.loggedin = false;
    AuthService.token = "null";
  }

  login(email: string, password: string) {
    //returns token
    this.api.login(email, password).subscribe((t) => {
      AuthService.token = t;
      window.localStorage.setItem("token", t);
      AuthService.loggedin = true;
      AuthService.loggedinSubject.next(AuthService.loggedin);
    })
  }

  loginWithToken() {
    let s: string | null = window.localStorage.getItem("token");
    if (typeof s === 'string') {
      this.api.loginWithToken(s).subscribe((t) => {
        AuthService.loggedin = true;
        AuthService.loggedinSubject.next(AuthService.loggedin);
      })
    }
  }

  signup(email: any, name: any, password: any, phone: any, address: any, floor: any, bell: any) {
    this.api.signup(email, name, password, phone, address, floor, bell).subscribe((c) => {
      console.log(c);
    });
  }

  health() {
    this.api.getHealth().subscribe((c) => {
      console.log(c);
    });
  }
}
