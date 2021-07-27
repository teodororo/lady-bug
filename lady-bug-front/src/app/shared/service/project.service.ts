import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { Project } from '../models/project.model';
import { map, catchError, flatMap } from 'rxjs/operators'
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProjectService {

  private apiPath: string = "http://25.98.20.55:3000/projects"

  constructor(private http: HttpClient) { }

  createProject(project: Project): Observable<Project> {
    return this.http.post(this.apiPath, project).pipe( // o category aqui siguinifica o corpo da requisicao post que esta sendo feita
      catchError(this.handleError),
      map(this.jsonDataToProject),
    )
  }


  private jsonDataToProject(jsonData: any): Project {
    return jsonData as Project;
  }

  private handleError(error: any): Observable<any> {
    console.log("ERRO NA REQUISIÇÃO => ", error);
    return throwError(error);
  }


}
