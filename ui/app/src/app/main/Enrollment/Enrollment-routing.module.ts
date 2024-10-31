import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EnrollmentHomeComponent } from './home/Enrollment-home.component';
import { EnrollmentNewComponent } from './new/Enrollment-new.component';
import { EnrollmentDetailComponent } from './detail/Enrollment-detail.component';

const routes: Routes = [
  {path: '', component: EnrollmentHomeComponent},
  { path: 'new', component: EnrollmentNewComponent },
  { path: ':id', component: EnrollmentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Enrollment-detail-permissions'
      }
    }
  }
];

export const ENROLLMENT_MODULE_DECLARATIONS = [
    EnrollmentHomeComponent,
    EnrollmentNewComponent,
    EnrollmentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EnrollmentRoutingModule { }