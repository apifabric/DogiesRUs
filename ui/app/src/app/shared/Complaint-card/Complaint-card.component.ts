import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Complaint-card.component.html',
  styleUrls: ['./Complaint-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Complaint-card]': 'true'
  }
})

export class ComplaintCardComponent {


}