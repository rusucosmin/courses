import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-authors-new',
  templateUrl: './authors-new.component.html',
  styleUrls: ['./authors-new.component.css']
})
export class AuthorsNewComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    console.log("authors - new")
  }

}
