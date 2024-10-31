import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WalkerService-card.component.html',
  styleUrls: ['./WalkerService-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WalkerService-card]': 'true'
  }
})

export class WalkerServiceCardComponent {


}