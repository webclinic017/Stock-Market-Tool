import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { InvestmentTypeComponent } from './investment-type/investment-type.component';
import { BuyRecListComponent } from './buy-rec-list/buy-rec-list.component';
import { BuyRecComponent } from './buy-rec-list/buy-rec/buy-rec.component';
import { RequestDetailsComponent } from './request-details/request-details.component';
import { StockComponent } from './stock/stock.component';
import { FundFormulaComponent } from './fund-formula/fund-formula.component';
import { FormulaInvestorComponent } from './fund-formula/formula-investor/formula-investor.component';
import { FundInvestorComponent } from './fund-formula/fund-investor/fund-investor.component';
import { LoginComponentComponent } from './authorization/login-component/login-component.component';
import { LoginComponent } from './authorization/login/login.component';
import { RegisterComponent } from './authorization/register/register.component';
import { CommExampleComponent } from './comm-example/comm-example.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    InvestmentTypeComponent,
    BuyRecListComponent,
    BuyRecComponent,
    RequestDetailsComponent,
    StockComponent,
    FundFormulaComponent,
    FormulaInvestorComponent,
    FundInvestorComponent,
    LoginComponentComponent,
    LoginComponent,
    RegisterComponent,
    CommExampleComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
