import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { BugRoutingModule } from './bug-routing.module';
import { BugComponent } from './bug.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    BugComponent
  ],
  imports: [
    CommonModule,
    BugRoutingModule,
    ReactiveFormsModule,
    FormsModule
  ]
})
export class BugModule { }
