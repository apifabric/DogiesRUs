import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WalkerService-new',
  templateUrl: './WalkerService-new.component.html',
  styleUrls: ['./WalkerService-new.component.scss']
})
export class WalkerServiceNewComponent {
  @ViewChild("WalkerServiceForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}