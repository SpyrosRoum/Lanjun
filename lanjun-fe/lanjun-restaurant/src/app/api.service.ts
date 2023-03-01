import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, throwError } from 'rxjs';

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
}
