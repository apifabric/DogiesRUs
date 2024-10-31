import { MenuRootItem } from 'ontimize-web-ngx';

import { AddressCardComponent } from './Address-card/Address-card.component';

import { ComplaintCardComponent } from './Complaint-card/Complaint-card.component';

import { DogCardComponent } from './Dog-card/Dog-card.component';

import { DogWalkCardComponent } from './DogWalk-card/DogWalk-card.component';

import { EnrollmentCardComponent } from './Enrollment-card/Enrollment-card.component';

import { FeedbackCardComponent } from './Feedback-card/Feedback-card.component';

import { IncidentCardComponent } from './Incident-card/Incident-card.component';

import { OwnerCardComponent } from './Owner-card/Owner-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { PromotionCardComponent } from './Promotion-card/Promotion-card.component';

import { ScheduleCardComponent } from './Schedule-card/Schedule-card.component';

import { ServiceCardComponent } from './Service-card/Service-card.component';

import { WalkCardComponent } from './Walk-card/Walk-card.component';

import { WalkerCardComponent } from './Walker-card/Walker-card.component';

import { WalkerServiceCardComponent } from './WalkerService-card/WalkerService-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Address', name: 'ADDRESS', icon: 'view_list', route: '/main/Address' }
    
        ,{ id: 'Complaint', name: 'COMPLAINT', icon: 'view_list', route: '/main/Complaint' }
    
        ,{ id: 'Dog', name: 'DOG', icon: 'view_list', route: '/main/Dog' }
    
        ,{ id: 'DogWalk', name: 'DOGWALK', icon: 'view_list', route: '/main/DogWalk' }
    
        ,{ id: 'Enrollment', name: 'ENROLLMENT', icon: 'view_list', route: '/main/Enrollment' }
    
        ,{ id: 'Feedback', name: 'FEEDBACK', icon: 'view_list', route: '/main/Feedback' }
    
        ,{ id: 'Incident', name: 'INCIDENT', icon: 'view_list', route: '/main/Incident' }
    
        ,{ id: 'Owner', name: 'OWNER', icon: 'view_list', route: '/main/Owner' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Promotion', name: 'PROMOTION', icon: 'view_list', route: '/main/Promotion' }
    
        ,{ id: 'Schedule', name: 'SCHEDULE', icon: 'view_list', route: '/main/Schedule' }
    
        ,{ id: 'Service', name: 'SERVICE', icon: 'view_list', route: '/main/Service' }
    
        ,{ id: 'Walk', name: 'WALK', icon: 'view_list', route: '/main/Walk' }
    
        ,{ id: 'Walker', name: 'WALKER', icon: 'view_list', route: '/main/Walker' }
    
        ,{ id: 'WalkerService', name: 'WALKERSERVICE', icon: 'view_list', route: '/main/WalkerService' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AddressCardComponent

    ,ComplaintCardComponent

    ,DogCardComponent

    ,DogWalkCardComponent

    ,EnrollmentCardComponent

    ,FeedbackCardComponent

    ,IncidentCardComponent

    ,OwnerCardComponent

    ,PaymentCardComponent

    ,PromotionCardComponent

    ,ScheduleCardComponent

    ,ServiceCardComponent

    ,WalkCardComponent

    ,WalkerCardComponent

    ,WalkerServiceCardComponent

];