import { Component, OnInit } from '@angular/core';
import {AuthorService} from "../../shared/author.service";
import {Author} from "../../shared/author.model";

@Component({
  selector: 'app-authors-list',
  templateUrl: './authors-list.component.html',
  styleUrls: ['./authors-list.component.css']
})
export class AuthorsListComponent implements OnInit {
  errorMessage: string;
  authors: Author[];
  selectedAuthor: Author;
  constructor(private authorService: AuthorService) { }

  ngOnInit() {
    this.getAuthors();
  }

  getAuthors() {
    this.authorService.getAuthors()
      .subscribe(
        authors => this.authors = authors,
        error => this.errorMessage = <any>error
      );
  }

  onSelect(author: Author) {
    this.selectedAuthor = author;
  }

}
