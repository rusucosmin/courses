import {Component, OnInit, Input} from '@angular/core';
import { Location } from '@angular/common';
import {ActivatedRoute, Params} from "@angular/router";
import {AuthorService} from "../../shared/author.service";
import {Author} from "../../shared/author.model";
import {Observable} from "rxjs";

@Component({
  selector: 'app-authors-detail',
  templateUrl: './authors-detail.component.html',
  styleUrls: ['./authors-detail.component.css']
})
export class AuthorsDetailComponent implements OnInit {
  author: Author;

  constructor(private authorSevice: AuthorService,
    private route: ActivatedRoute,
    private location: Location) { }

  ngOnInit() {
    this.route.params
      .switchMap((params: Params) => this.getAuthor(Number(+params['id'])))
      .subscribe(author => {
        console.log("got author: ");
        console.log(author);
        this.author = author;
        this.author.books = this.author.books.sort((n1, n2) => n1.year - n2.year);
      });
  }

  getAuthor(id: number) : Observable<Author> {
    return this.authorSevice.getAuthors()
      .map(arr => arr.filter(au => au.id == id)[0])
  }





}
