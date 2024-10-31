import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ComplaintHomeComponent } from './home/Complaint-home.component';
import { ComplaintNewComponent } from './new/Complaint-new.component';
import { ComplaintDetailComponent } from './detail/Complaint-detail.component';

const routes: Routes = [
  {path: '', component: ComplaintHomeComponent},
  { path: 'new', component: ComplaintNewComponent },
  { path: ':id', component: ComplaintDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Complaint-detail-permissions'
      }
    }
  }
];

export const COMPLAINT_MODULE_DECLARATIONS = [
    ComplaintHomeComponent,
    ComplaintNewComponent,
    ComplaintDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ComplaintRoutingModule { }