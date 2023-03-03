import { HttpClient, HttpErrorResponse, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, throwError } from 'rxjs';
import { AuthService } from './auth.service';

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
    }
    return throwError(error);
  }

  private extractData(res: any) {
    let body = res;
    return body || {};
  }

  public getItems(): Observable<any> {
    let headers: HttpHeaders = this.headers;
    return this.http.get("http://135.181.25.134:8080/v1/items", { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
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

  public addItem(n: string | undefined, i: string | undefined, d: string | undefined, p: number | undefined, c: string | undefined): Observable<any> {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    headers = headers.append('Authorization', AuthService.token);
    const json = JSON.stringify({ name: n, image_url: i, description: d, category: c, price: p });

    return this.http.post("http://135.181.25.134:8080/v1/items", json, { headers }).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }

  public deleteItem(id: string): Observable<any> {
    let headers: HttpHeaders = this.headers;
    headers = headers.append('Content-Type', 'application/json');
    headers = headers.append('Authorization', AuthService.token);

    let httpParams = new HttpParams().set('id', id);

    let options = { params: httpParams, headers: headers };

    return this.http.delete("http://135.181.25.134:8080/v1/items", options).pipe(
      map(this.extractData),
      catchError(this.handleError)
    );
  }
}
