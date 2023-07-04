import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BooksService {

  constructor(private http: HttpClient) { }

  books() {
    let httpOptions = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Headrs': 'Content-Type',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'no-cache',
        'Access-Control-Allowed-Methods': 'GET'
      })
    };

    // return this.http.post(url, payload, httpOptions);
    return this.http.get('http://localhost:5000/books', httpOptions);
  }

  recommendedBooks(book_liked: string) {
    let httpOptions = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Headrs': 'Content-Type',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'no-cache',
        'Access-Control-Allowed-Methods': 'GET'
      })
    };

    let url = `http://localhost:5000/book_recommendations?book_liked=${book_liked}`
    return this.http.get(url, httpOptions);
  }


}
