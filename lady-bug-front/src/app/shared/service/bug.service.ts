import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { map, catchError, flatMap } from 'rxjs/operators'
import { HttpClient } from '@angular/common/http';
import { Bug } from '../models/bug.model';

@Injectable({
  providedIn: 'root'
})
export class BugService {

  private apiPath: string = "http://25.98.20.55:3000/bugs"

  constructor(private http: HttpClient) { }

  createBug(bug: Bug): Observable<Bug> {
    return this.http.post(this.apiPath, bug).pipe( // o category aqui siguinifica o corpo da requisicao post que esta sendo feita
      catchError(this.handleError),
      map(this.jsonDataToBug),
    )
  }


  private jsonDataToBug(jsonData: any): Bug {
    return jsonData as Bug;
  }

  private handleError(error: any): Observable<any> {
    console.log("ERRO NA REQUISIÇÃO => ", error);
    return throwError(error);
  }


}