import { Component, OnInit } from '@angular/core';
import { BooksService } from 'src/app/services/books.service';

@Component({
  selector: 'app-recommendations',
  templateUrl: './recommendations.component.html',
  styleUrls: ['./recommendations.component.scss']
})
export class RecommendationsComponent implements OnInit {
  books: any;
  likedBook: any;
  recommendedBooks: any;
  recommendedBooksLoading: boolean = false;
  constructor(private booksService: BooksService) { }

  ngOnInit(): void {
    this.booksService.books().subscribe((res: any)=> {
      this.books = res;
      console.log(this.books)
    })
  }

  onChangeLikedBook(e:any){
    let input = e.value?.['Book-Title'];
    if (input) {
      this.recommendedBooksLoading = true;
      this.booksService.recommendedBooks(input).subscribe((res:any)=> {
        this.recommendedBooks = res;
        this.recommendedBooksLoading = false;
      })
    } else {
      this.recommendedBooks = [];
    }
  }
}
