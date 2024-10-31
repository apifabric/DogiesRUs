import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'DogWalk-new',
  templateUrl: './DogWalk-new.component.html',
  styleUrls: ['./DogWalk-new.component.scss']
})
export class DogWalkNewComponent {
  @ViewChild("DogWalkForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}