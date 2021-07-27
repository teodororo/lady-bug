import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { Project } from '../shared/models/project.model';
import { ProjectService } from '../shared/service/project.service';

@Component({
  selector: 'app-project',
  templateUrl: './project.component.html',
  styleUrls: ['./project.component.scss']
})
export class ProjectComponent implements OnInit, OnDestroy {

  projectForm!: FormGroup; 
  private unsubscribe$ = new Subject<void>();
  member = ''; 
  qtdMember = 0;
  projectName = '';
  test = '';
  qtdTest = 0;

  constructor(
    private formBuilder: FormBuilder,
    private projectService: ProjectService,
    private toastr: ToastrService,
  ) { 

  }



  ngOnInit(): void {
    this.buildProjectForm();
  }

  ngOnDestroy() {
    this.unsubscribe$.next();
    this.unsubscribe$.complete();
  }

  private buildProjectForm() {
    this.projectForm = this.formBuilder.group({
      name: [null, [Validators.required]],
      client: [null, [Validators.required]],
      description: [null, [Validators.required]],
      team: this.formBuilder.array([]),

      testSuitename: [null, [Validators.required]],
      testSuiteDescription: [null, [Validators.required]],
      testSuiteInportance: [null, [Validators.required]],
      testesCases: this.formBuilder.array([]),
      testSuiteSteps: [null, [Validators.required]],
      testSuitePreConditions: [null, [Validators.required]],
    })
  }

  public createMember(value: string): FormGroup {
    return this.formBuilder.group({
      email: [value]
    })
  }

  public createTestCase(value: string): FormGroup {
    return this.formBuilder.group({
      description: [value]
    })
  }

  public addTestCase() {
    const control = this.projectForm.get('testesCases') as FormArray;
    control.push(this.createTestCase(this.test));
    this.qtdTest += 1;
    this.test = '';
  }


  public addMember() {
    const control = this.projectForm.get('team') as FormArray;
    control.push(this.createMember(this.member));
    this.qtdMember += 1;
    this.member = '';
  }

  onKey(event: any) { // without type info
    this.member = event.target.value;
  }

  onTest(event: any) { // without type info
    this.test = event.target.value;
  }


  createProject() {
    const project: Project = Object.assign(new Project, this.projectForm.value);

    this.projectService.createProject(project)
      .subscribe(
        project => {
          this.toastr.success('The project was successfully created', 'Success!');
          console.log('Projeto Cadastrado');
          this.projectForm.reset();
          this.member = '';
        },
        error => {
          console.log(error);
        }
      )
  }

  setProjectName(event: any) {
    this.projectName = event.target.value;
  }



}
