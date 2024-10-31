import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './DogWalk-card.component.html',
  styleUrls: ['./DogWalk-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.DogWalk-card]': 'true'
  }
})

export class DogWalkCardComponent {


}