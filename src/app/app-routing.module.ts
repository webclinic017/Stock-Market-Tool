import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import { LoginComponent } from './authorization/login/login.component';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { SecurityAnalysisComponent } from './security-analysis/security-analysis.component';
import { MarketAnalysisComponent } from './market-analysis/market-analysis.component';

const appRoutes: Routes =
[
    {
        path: '',
        redirectTo: '/home',
        pathMatch: 'full'
    },
    {
        path: 'home',
        component: HomeComponent,
    },
    {
        path: 'about',
        component: AboutComponent,
    },
    {
        path: 'login',
        component: LoginComponent,
    },
    {
        path: 'market-analysis',
        component: MarketAnalysisComponent,
    },
    {
        path: 'security-analysis',
        component: SecurityAnalysisComponent,
    }
];

@NgModule
({
    imports: [RouterModule.forRoot(appRoutes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
