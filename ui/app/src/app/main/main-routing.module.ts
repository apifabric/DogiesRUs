import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Address', loadChildren: () => import('./Address/Address.module').then(m => m.AddressModule) },
    
        { path: 'Complaint', loadChildren: () => import('./Complaint/Complaint.module').then(m => m.ComplaintModule) },
    
        { path: 'Dog', loadChildren: () => import('./Dog/Dog.module').then(m => m.DogModule) },
    
        { path: 'DogWalk', loadChildren: () => import('./DogWalk/DogWalk.module').then(m => m.DogWalkModule) },
    
        { path: 'Enrollment', loadChildren: () => import('./Enrollment/Enrollment.module').then(m => m.EnrollmentModule) },
    
        { path: 'Feedback', loadChildren: () => import('./Feedback/Feedback.module').then(m => m.FeedbackModule) },
    
        { path: 'Incident', loadChildren: () => import('./Incident/Incident.module').then(m => m.IncidentModule) },
    
        { path: 'Owner', loadChildren: () => import('./Owner/Owner.module').then(m => m.OwnerModule) },
    
        { path: 'Payment', loadChildren: () => import('./Payment/Payment.module').then(m => m.PaymentModule) },
    
        { path: 'Promotion', loadChildren: () => import('./Promotion/Promotion.module').then(m => m.PromotionModule) },
    
        { path: 'Schedule', loadChildren: () => import('./Schedule/Schedule.module').then(m => m.ScheduleModule) },
    
        { path: 'Service', loadChildren: () => import('./Service/Service.module').then(m => m.ServiceModule) },
    
        { path: 'Walk', loadChildren: () => import('./Walk/Walk.module').then(m => m.WalkModule) },
    
        { path: 'Walker', loadChildren: () => import('./Walker/Walker.module').then(m => m.WalkerModule) },
    
        { path: 'WalkerService', loadChildren: () => import('./WalkerService/WalkerService.module').then(m => m.WalkerServiceModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }