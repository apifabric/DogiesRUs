import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DogWalkHomeComponent } from './home/DogWalk-home.component';
import { DogWalkNewComponent } from './new/DogWalk-new.component';
import { DogWalkDetailComponent } from './detail/DogWalk-detail.component';

const routes: Routes = [
  {path: '', component: DogWalkHomeComponent},
  { path: 'new', component: DogWalkNewComponent },
  { path: ':id', component: DogWalkDetailComponent,
    data: {
      oPermission: {
        permissionId: 'DogWalk-detail-permissions'
      }
    }
  }
];

export const DOGWALK_MODULE_DECLARATIONS = [
    DogWalkHomeComponent,
    DogWalkNewComponent,
    DogWalkDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DogWalkRoutingModule { }