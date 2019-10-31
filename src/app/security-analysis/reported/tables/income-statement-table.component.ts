import { Component, ViewChild, OnInit, Input, AfterViewInit } from '@angular/core';
import { MatTableDataSource, MatPaginator } from '@angular/material';
import { IncomeSheet } from '../../../server-communication/app-endpoint.constants';
import { ReportedService } from '../reported.service';

@Component({
    selector: 'app-income-statement-table',
    template: `
        <div class="mat-elevation-z8">
            <smt-income-one *ngIf="displayTable1" [incomeSheet]="incomeSheets[0][0]"></smt-income-one>
            <smt-income-two *ngIf="displayTable2"></smt-income-two>
            <smt-income-three *ngIf="displayTable3"></smt-income-three>
            <smt-income-four *ngIf="displayTable4"></smt-income-four>
            <smt-income-five *ngIf="displayTable5"></smt-income-five>
        </div>
        <div class="center-buttons">
            <button (click)="displayTable(1)" class="btn btn-primary">1999-2002</button>
            <button (click)="displayTable(2)" class="btn btn-primary">2003-2006</button>
            <button (click)="displayTable(3)" class="btn btn-primary">2007-2010</button>
            <button (click)="displayTable(4)" class="btn btn-primary">2011-2014</button>
            <button (click)="displayTable(5)" class="btn btn-primary">2015-2018</button>
        </div>
    `,
    styleUrls: ['table.scss']
})
export class IncomeStatementTableComponent implements OnInit {
    // State booleans.
    public displayTable1 = true;
    public displayTable2 = false;
    public displayTable3 = false;
    public displayTable4 = false;
    public displayTable5 = false;

    public incomeSheets: IncomeSheet[][];

    constructor(public reportedService: ReportedService) {
        this.incomeSheets = this.reportedService.getIncomeTables();
    }

    ngOnInit() { }

    public displayTable(table: number) {
        if (table === 1) {
            this.displayTable1 = true;
            this.displayTable2 = false;
            this.displayTable3 = false;
            this.displayTable4 = false;
            this.displayTable5 = false;

        } if (table === 2) {
            this.displayTable1 = false;
            this.displayTable2 = true;
            this.displayTable3 = false;
            this.displayTable4 = false;
            this.displayTable5 = false;

        } if (table === 3) {
            this.displayTable1 = false;
            this.displayTable2 = false;
            this.displayTable3 = true;
            this.displayTable4 = false;
            this.displayTable5 = false;

        } if (table === 4) {
            this.displayTable1 = false;
            this.displayTable2 = false;
            this.displayTable3 = false;
            this.displayTable4 = true;
            this.displayTable5 = false;

        } if (table === 5) {
            this.displayTable1 = false;
            this.displayTable2 = false;
            this.displayTable3 = false;
            this.displayTable4 = false;
            this.displayTable5 = true;
        }
    }
}

/*export interface PeriodicElement {
    metric: string;
    name: number;
    weight: number;
    symbol: number;
    value: number;
}

const INCOME_SHEET = [
    {metric: 'Revenue', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Other Revenue', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'XO & Accounting Changes', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Other Operating Income', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Income Tax', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Basic Weighted Avg Shares', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Income (Loss) from Cont Ops', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Cost of Revenue', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Current Income Tax', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Diluted Weighted Avg Shares', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Discontinued Operations', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Foreign Exch (Gain) Loss', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Current Income Tax', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Cost of Goods & Services', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Income (Loss) from Cont Ops', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Cost of Revenue', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Current Income Tax', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Non-Operating (Income) Loss', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
];

const BALANCE_SHEET = [
    {metric: 'Accumulated Depreciation', value: balanceSheet.accDeprec},
    {metric: 'Accrued Taxes', value: balanceSheet.accruedTaxes},
    {metric: 'Accounts & Notes Receivable', value: balanceSheet.acctsRec},
    {metric: 'Accounts Receivable, Net', value: balanceSheet.acctsRecNet},
    {metric: 'Accrued Liabilities', value: balanceSheet.accuredLiab},
    {metric: 'Additional Paid in Capital', value: balanceSheet.addPaidCap},
    {metric: 'Cash & Cash Equivalents', value: balanceSheet.cashEq},
    {metric: 'Cash, Cash Equivalents & STI', value: balanceSheet.cashEqSti},
    {metric: 'Common Stock', value: balanceSheet.commonStock},
    {metric: 'Current Portion of LT Debt', value: balanceSheet.currLtDebt},
    {metric: 'Deferred Tax Liabilities', value: balanceSheet.defTabLiab},
    {metric: 'Deferred Revenue', value: balanceSheet.deffRev1},
    {metric: 'Deferred Tax Assets', value: balanceSheet.deffTaxAssets},
    {metric: 'Derivatives & Hedging', value: balanceSheet.derivHedge1},
    {metric: 'Derivative & Hedging Assets', value: balanceSheet.derivHedgeAssets1},
    {metric: 'Equity Before Minority Interest', value: balanceSheet.equityBeforeMinInt},
    {metric: 'Finished Goods', value: balanceSheet.finGoods},
    {metric: 'Goodwill', value: balanceSheet.goodwill},
    {metric: 'Interest & Dividends Payable', value: balanceSheet.intDivsPayables},
    {metric: 'Inventories', value: balanceSheet.inv},
    {metric: 'Total Liabilities & Equity', value: balanceSheet.liabAndEquity},
    {metric: 'LT Borrowings', value: balanceSheet.ltBorrow},
    {metric: 'LT Debt', value: balanceSheet.ltDebt},
    {metric: 'LT Finance Leases', value: balanceSheet.ltFinLeases},
    {metric: 'LT Investments & Receivables', value: balanceSheet.ltiReceivables},
    {metric: 'Minority/Non Controlling Interest', value: balanceSheet.minNonControlInt},
    {metric: 'Misc LT Assets', value: balanceSheet.miscAssets},
    {metric: 'Misc LT Liabilities', value: balanceSheet.miscLtLiab},
    {metric: 'Misc ST Assets', value: balanceSheet.miscStAssets},
    {metric: 'Misc ST Liabilities', value: balanceSheet.miscStLiab},
    {metric: 'Notes Receivable, Net', value: balanceSheet.notesRecNet},
    {metric: 'Other Equity', value: balanceSheet.othEquity},
    {metric: 'Other Intangible Assets', value: balanceSheet.othIntAssets},
    {metric: 'Other Inventory', value: balanceSheet.othInv},
    {metric: 'Other LT Assets', value: balanceSheet.othLtAssets},
    {metric: 'Other LT Liabilities', value: balanceSheet.othLtLiab},
    {metric: 'Other Payables & Accruals', value: balanceSheet.othPayablesAccurals},
    {metric: 'Other ST Assets', value: balanceSheet.othStAssets},
    {metric: 'Other ST Liabilities', value: balanceSheet.othStLiab},
    {metric: 'Accounts Payable', value: balanceSheet.payables},
    {metric: 'Payables & Accruals', value: balanceSheet.payablesAccruals},
    {metric: 'Pension Liabilities', value: balanceSheet.pensionLiab},
    {metric: 'Property, Plant & Equip', value: balanceSheet.ppe},
    {metric: 'Property, Plant & Equip, Net', value: balanceSheet.ppeNet},
    {metric: 'Preferred Equity and Hybrid Capital', value: balanceSheet.prefEquityHybridCap},
    {metric: 'Raw Materials', value: balanceSheet.rawMat},
    {metric: 'Retained Earnings', value: balanceSheet.re},
    {metric: 'Share Capital & APIC', value: balanceSheet.shareCapApic},
    {metric: 'ST Borrowings', value: balanceSheet.stBorrowings},
    {metric: 'ST Debt', value: balanceSheet.stDebt},
    {metric: 'ST Finance Leases', value: balanceSheet.stFinLeases},
    {metric: 'Cash, Cash Equivalents & STI', value: balanceSheet.sti},
    {metric: 'Total Assets', value: balanceSheet.totalAssets1},
    {metric: 'Total Current Assets', value: balanceSheet.totalCurrAssets},
    {metric: 'Total Current Liabilities', value: balanceSheet.totalCurrLiab},
    {metric: 'Total Equity', value: balanceSheet.totalEquity},
    {metric: 'Total Intangible Assets', value: balanceSheet.totalIntAssets},
    {metric: 'Total Liabilities', value: balanceSheet.totalLiab},
    {metric: 'Total Noncurrent Assets', value: balanceSheet.totalNonCurrAssets},
    {metric: 'Total Noncurrent Liabilities', value: balanceSheet.totalNonCurrLiab},
    {metric: 'Treasury Stock', value: balanceSheet.treasuryStock},
    {metric: 'Work In Process', value: balanceSheet.wip},
]

const CASHFLOW_SHEET = [
    {metric: 'Acq of Fixed & Intang', value: acqFixedIntag},
    {metric: 'Acq of Fixed Prod Assets', value: acqFixedProdAssets},
    {metric: 'Acq of Intangible Assets', value: acqIntagAssets},
    {metric: 'Cash for Acq of Subs', value: cashAcqSubs},
    {metric: 'Cash from Divestitures', value: cashDivest},
    {metric: 'Cash from Financing Activities', value: cashFinAct2},
    {metric: 'Cash from Investing Activities', value: cashInvestAct1},
    {metric: 'Cash for JVs', value: cashJvs},
    {metric: 'Cash From LT Debt', value: cashLtDebt},
    {metric: 'Cash from Operating Activities', value: cashOpAct},
    {metric: 'Cash Paid for Interest', value: cashPaidInt},
    {metric: 'Cash Paid for Taxes', value: cashPaidTaxes},
    {metric: 'Cash From (Repayment) Debt', value: cashRepayDebt},
    {metric: 'Cash (Repurchase) of Equity', value: cashRepurchEquity},
    {metric: 'Cash From (Repay) ST Debt', value: cashStDebt},
    {metric: 'Inc (Dec) in Accts Payable', value: chgAcctsRec},
    {metric: 'Change in Fixed & Intang', value: chgFixedIntang},
    {metric: '(Inc) Dec in Inventories', value: chgInventories},
    {metric: 'Chg in Non-Cash Work Cap', value: chgNonCashOp},
    {metric: 'Inc (Dec) in Other', value: chgOther},
    {metric: 'Decrease in Capital Stock', value: decCapitalStock},
    {metric: 'Dec in LT Investment', value: decLtInvest},
    {metric: 'Deferred Income Taxes', value: defIntComp},
    {metric: 'Depreciation & Amortization', value: depreAmort},
    {metric: 'Disp in Fixed & Intang', value: dispFixedIntang},
    {metric: 'Disp of Fixed Prod Assets', value: dispFixedProdAssets},
    {metric: 'Disp of Intangible Asset', value: dispIntagAssets},
    {metric: 'Dividends Paid', value: divsPaid},
    {metric: 'Effect of Foreign Exchange Rates', value: effectForexRates},
    {metric: 'Increase in Capital Stock', value: incCapitalStock},
    {metric: 'Inc in LT Investment', value: incLtInvest},
    {metric: 'Net Cash From Acq & Div', value: netCashAcqDiv},
    {metric: 'Net Cash From Disc Ops', value: netCashDiscOps1},
    {metric: 'Net Changes in Cash', value: netChgCash},
    {metric: 'Net Change in LT Investment', value: netChgLtInvest},
    {metric: 'Net Income', value: niCf},
    {metric: 'Non-Cash Items', value: nonCashItems},
    {metric: 'Other Financing Activities', value: othFinAct},
    {metric: 'Other Investing Activities', value: othInvestAct},
    {metric: 'Other Non-Cash Adj', value: othNonCashAdj},
    {metric: 'Repayments of LT Debt', value: repayLtDebt},
    {metric: 'Stock-Based Compensation', value: stockComp}
]

*/
