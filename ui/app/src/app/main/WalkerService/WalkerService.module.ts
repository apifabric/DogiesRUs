import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WALKERSERVICE_MODULE_DECLARATIONS, WalkerServiceRoutingModule} from  './WalkerService-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WalkerServiceRoutingModule
  ],
  declarations: WALKERSERVICE_MODULE_DECLARATIONS,
  exports: WALKERSERVICE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WalkerServiceModule { }