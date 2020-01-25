import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of ,empty} from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { MessageService } from './message.service';
import { environment } from '../environments/environment';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({ providedIn: 'root' })
export class DTSCService {
  private querytUrl = environment.APIEndpoint+'/diseases';  // URL to web api

  constructor(
    private http: HttpClient,
    private messageService: MessageService) { }

  clusterQuery (disease,area): Observable<any> {
      return this.http.get<any>(this.querytUrl+"?disease="+disease+"&area="+area)
        .pipe(
          tap(_ => this.log('fetched results')),
          catchError(this.handleError<any>('getResult', []))
        );
  }
  

 

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  /** Log a ReportService message with the MessageService */
  private log(message: string) {
    this.messageService.add(`DTSCService: ${message}`);
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at http://angular.io/license
*/