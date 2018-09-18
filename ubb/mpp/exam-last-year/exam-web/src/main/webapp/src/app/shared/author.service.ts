import {Http, Response, Headers} from "@angular/http";
import {Observable} from "rxjs";
import {Author} from "./author.model";

import 'rxjs/add/operator/catch';

import 'rxjs/add/operator/map';
import {Injectable} from "@angular/core";

/**
 * Created by cosmin on 12/06/2017.
 */
@Injectable()
export class AuthorService {
  private authorsUrl = 'http://localhost:8080/api/authors';
  private header = new Headers({"Content-Type": "application/json"});

  constructor(private http: Http) {}

  getAuthors(): Observable<Author[]> {
    return this.http.get(this.authorsUrl)
      .map(this.extractData)
      .catch(this.handleError);
  }

  private extractData(res: Response) {
    let body = res.json();
    return body.authors || {};
  }
  private handleError(error: Response | any) {
    console.log("handleError: " + error);
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
    } else {
      errMsg = error.message ? error.message : error.toString();
    }
    console.error(errMsg);
    return Observable.throw(errMsg);
  }
}
