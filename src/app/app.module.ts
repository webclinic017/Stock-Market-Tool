import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { AboutComponent } from './about/about.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './authorization/login/login.component';
import { LogoutComponent } from './authorization/logout/logout.component';
import { AppRoutingModule } from './app-routing.module';
import { MarketAnalysisComponent } from './market-analysis/market-analysis.component';
import { SecurityAnalysisComponent } from './security-analysis/security-analysis.component';

@NgModule({
    declarations: [
        AppComponent,
        HeaderComponent,
        AboutComponent,
        HomeComponent,
        LoginComponent,
        LogoutComponent,
        MarketAnalysisComponent,
        SecurityAnalysisComponent,
    ],
    imports: [
        BrowserModule,
        AppRoutingModule
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule { }
