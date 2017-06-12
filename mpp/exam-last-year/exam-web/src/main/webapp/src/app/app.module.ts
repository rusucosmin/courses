import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { AuthorsComponent } from './authors/authors.component';
import { AuthorsListComponent } from './authors/authors-list/authors-list.component';
import { AuthorsDetailComponent } from './authors/authors-detail/authors-detail.component';
import { AuthorsNewComponent } from './authors/authors-new/authors-new.component';
import {AuthorService} from './shared/author.service'


@NgModule({
  declarations: [
    AppComponent,
    AuthorsComponent,
    AuthorsListComponent,
    AuthorsDetailComponent,
    AuthorsNewComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule
  ],
  providers: [AuthorService],
  bootstrap: [AppComponent]
})
export class AppModule { }
