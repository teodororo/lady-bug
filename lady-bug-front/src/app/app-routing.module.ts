import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'project',
    loadChildren: () =>
      import('./project/project.module').then(
        (m) => m.ProjectModule
      ),
  },
  {
    path: 'bug',
    loadChildren: () =>
      import('./bug/bug.module').then(
        (m) => m.BugModule
      ),
  },
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
