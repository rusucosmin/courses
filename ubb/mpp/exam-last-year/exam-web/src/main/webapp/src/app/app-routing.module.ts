import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AppComponent} from "./app.component";
import {AuthorsComponent} from "./authors/authors.component";
import {AuthorsDetailComponent} from "./authors/authors-detail/authors-detail.component";
import {AuthorsNewComponent} from "./authors/authors-new/authors-new.component";

const routes: Routes = [
    { path: 'ab/authors',     component: AuthorsComponent },
    { path: 'ab/authors/new', component: AuthorsNewComponent},
    { path: 'ab/authors/:id', component: AuthorsDetailComponent},
];

@NgModule({
    imports: [ RouterModule.forRoot(routes) ],
    exports: [ RouterModule ]
})
export class AppRoutingModule {}
