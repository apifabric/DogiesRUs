import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {DOGWALK_MODULE_DECLARATIONS, DogWalkRoutingModule} from  './DogWalk-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    DogWalkRoutingModule
  ],
  declarations: DOGWALK_MODULE_DECLARATIONS,
  exports: DOGWALK_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DogWalkModule { }