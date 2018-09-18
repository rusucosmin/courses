import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-authors',
  templateUrl: './authors.component.html',
  styleUrls: ['./authors.component.css']
})
export class AuthorsComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  add() {
    console.log("merge");
    this.router.navigate(['ab/authors/new'])
  }
}
