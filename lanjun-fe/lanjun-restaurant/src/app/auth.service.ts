import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { ApiService } from './api.service';
import { User } from './user.model';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  static user: User = new User();
  static loggedin: boolean;
  static token: string;
  static loggedinSubject: Subject<boolean> = new Subject();

  constructor(private api: ApiService) {
    AuthService.loggedin = false;
    AuthService.token = "null";
  }

  login(email: string, password: string) {
    this.api.login(email, password).subscribe((t) => {
      this.loginData(t);
    })
  }

  loginWithToken() {
    let s: string | null = window.localStorage.getItem("token");
    if (typeof s === 'string') {
      this.api.loginWithToken(s).subscribe((t) => {
        this.loginData(t);
      })
    }
  }

  private loginData(t: any) {
    AuthService.token = t.token;
    window.localStorage.setItem("token", t);
    AuthService.loggedin = true;
    AuthService.loggedinSubject.next(AuthService.loggedin);
    this.api.me().subscribe((u) => {
      AuthService.user.email = u.email;
      AuthService.user.name = u.name;
      AuthService.user.address = u.address;
      AuthService.user.floor = u.floor;
      AuthService.user.bell = u.bell;
      AuthService.user.phone = u.phone;
      AuthService.user.admin = u.type === 'admin';
    });
  }

  signup(email: any, name: any, password: any, phone: any, address: any, floor: any, bell: any) {
    this.api.signup(email, name, password, phone, address, floor, bell).subscribe((c) => {
      this.api.login(email, password)
    });
  }

  health() {
    this.api.getHealth().subscribe((c) => {
      console.log(c);
    });
  }
}
