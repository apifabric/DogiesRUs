import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {COMPLAINT_MODULE_DECLARATIONS, ComplaintRoutingModule} from  './Complaint-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ComplaintRoutingModule
  ],
  declarations: COMPLAINT_MODULE_DECLARATIONS,
  exports: COMPLAINT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ComplaintModule { }