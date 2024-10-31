import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkerServiceHomeComponent } from './home/WalkerService-home.component';
import { WalkerServiceNewComponent } from './new/WalkerService-new.component';
import { WalkerServiceDetailComponent } from './detail/WalkerService-detail.component';

const routes: Routes = [
  {path: '', component: WalkerServiceHomeComponent},
  { path: 'new', component: WalkerServiceNewComponent },
  { path: ':id', component: WalkerServiceDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WalkerService-detail-permissions'
      }
    }
  }
];

export const WALKERSERVICE_MODULE_DECLARATIONS = [
    WalkerServiceHomeComponent,
    WalkerServiceNewComponent,
    WalkerServiceDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkerServiceRoutingModule { }