import { HttpClient, HttpErrorResponse, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, throwError } from 'rxjs';
import { AuthService } from './auth.service';
import { CartItemSimple } from './cart-item-simple.model';
import { CartItem } from './cart-item.model';
import { Reservation } from './reservation.model';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private headers: HttpHeaders;
  constructor(private http: HttpClient) {
    this.headers = new HttpHeaders();
    this.headers = this.headers.append('Access-Control-Allow-Origin', "*");
  }

  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      console.error("An error occurred:", error.error.message);
    } else {
      console.error(
        `Backend returned code ${error.status}, ` + `body was: ${error.error}`
      );
      console.error(error);

    }
    return throwError(error);
  }

  private extractData(res: any) {
    let body = res;
    return body || {};
  }

  public getHealth(): Observable<any> {
    let headers: HttpHeaders = this.headers;
    return this.http.get("http://135.181.25.134:8080/health", { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public signup(email: string, name: string, password: string, phone: string, address: string, floor: string, bell: string): Observable<any> {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    const json = JSON.stringify({ email: email, name: name, password: password, phone: phone, address: address, floor: floor, bell: bell });

    return this.http.post("http://135.181.25.134:8080/v1/sign_up", json, { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public login(email: string, password: string): Observable<any> {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    const json = JSON.stringify({ email: email, password: password });

    return this.http.post("http://135.181.25.134:8080/v1/login", json, { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public loginWithToken(token: string): Observable<any> {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    const json = JSON.stringify({ token: token });

    //TODO Change to login with token 
    return this.http.post("http://135.181.25.134:8080/v1/login", json, { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public me() {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    headers = headers.append('Authorization', `Bearer ${AuthService.token}`);
    console.log(AuthService.token);

    return this.http.get("http://135.181.25.134:8080/v1/users/me", { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public getItems(): Observable<any> {
    let headers: HttpHeaders = this.headers;
    return this.http.get("http://135.181.25.134:8080/v1/items", { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public addItem(n: string | undefined, i: string | undefined, d: string | undefined, p: number | undefined, c: string | undefined): Observable<any> {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    headers = headers.append('Authorization', `Bearer ${AuthService.token}`);

    const json = JSON.stringify({ name: n, image_url: i, description: d, category: c, price: p });

    return this.http.post("http://135.181.25.134:8080/v1/items", json, { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public deleteItem(id: string): Observable<any> {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    headers = headers.append('Authorization', `Bearer ${AuthService.token}`);

    return this.http.delete(`http://135.181.25.134:8080/v1/items/${id}/`, { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public updateItem(id: string, n: string, i: string, d: string, p: number, c: string): Observable<any> {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    headers = headers.append('Authorization', `Bearer ${AuthService.token}`);

    const json = JSON.stringify({ id: id, name: n, image_url: i, description: d, category: c, price: p });

    return this.http.put("http://135.181.25.134:8080/v1/items", json, { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public getOrders(): Observable<any> {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    headers = headers.append('Authorization', `Bearer ${AuthService.token}`);

    return this.http.get('http://135.181.25.134:8080/v1/orders', { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public postOrder(token: string, sum: number, prepaid: boolean, cartItems: CartItem[], reservationR: Reservation): Observable<any> {
    let cis: CartItemSimple[] = new Array();
    cartItems.forEach(ci => {
      let _cis: CartItemSimple = new CartItemSimple(ci.item.id, ci.count);
      cis.push(_cis);
    })

    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    headers = headers.append('Authorization', `Bearer ${AuthService.token}`);

    return this.http.post('http://135.181.25.134:8080/v1/orders', { items: cis }, { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public deleteOrder(id: string) {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    headers = headers.append('Authorization', `Bearer ${AuthService.token}`);

    return this.http.delete(`http://135.181.25.134:8080/v1/orders/${id}/`, { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }
}
