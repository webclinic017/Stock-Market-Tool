import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule} from '@angular/common/http';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { AboutComponent } from './about/about.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './authorization/login.component';
import { AppRoutingModule } from './app-routing.module';
import { MarketAnalysisComponent } from './market-analysis/market-analysis.component';
import { SecurityAnalysisComponent } from './security-analysis/security-analysis.component';
import { AuthComponent } from './authorization/auth.component';
import { RegisterComponent } from './authorization/register.component';
import { FormsModule } from '@angular/forms';


@NgModule({
    declarations: [
        AppComponent,
        HeaderComponent,
        AboutComponent,
        HomeComponent,
        AuthComponent,
        LoginComponent,
        RegisterComponent,
        MarketAnalysisComponent,
        SecurityAnalysisComponent,
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        FormsModule
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule { }
