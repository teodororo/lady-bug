import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { Bug } from '../shared/models/bug.model';
import { BugService } from '../shared/service/bug.service';

@Component({
  selector: 'app-bug',
  templateUrl: './bug.component.html',
  styleUrls: ['./bug.component.scss']
})
export class BugComponent implements OnInit {

  bugForm!: FormGroup; 
  private unsubscribe$ = new Subject<void>();

  constructor(
    private formBuilder: FormBuilder,
    private bugService: BugService,
    private toastr: ToastrService,
  ) { }

  ngOnInit(): void {
    this.buidBugForm();
  }

  ngOnDestroy() {
    this.unsubscribe$.next();
    this.unsubscribe$.complete();
  }

  private buidBugForm() {
    this.bugForm = this.formBuilder.group({
      testSuitename: [null],
      testesCases: [null],
      developer: [null],
      observations: [null],
    })
  }

  createBug() {
    const bug: Bug = Object.assign(new Bug, this.bugForm.value);

    this.bugService.createBug(bug)
      .subscribe(
        bug => {
          this.toastr.success('The project was successfully created', 'Success!');
          console.log('Projeto Cadastrado');
          this.bugForm.reset();
        },
        error => {
          console.log(error);
        }
      )
  }

}
