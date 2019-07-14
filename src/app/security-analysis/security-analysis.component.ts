import { Component, OnInit } from '@angular/core';
export enum FinancialsDisplayEnum {
    'Healthy',
    'Unhealthy'
}

// TODO: Get real values from Jimmy.
export enum FinacialsEnum {
    Healthy,
    Unhealthy
}

// TODO: Replicate on backend.
export class OwnerSummary {
    public intrinsicValue: number;
    public oneYearGrowth: number;
    public fiveYearGrowth: number;
    public historicFin: FinacialsEnum;
    public acuteFin: FinacialsEnum;
    public projectedFin: FinacialsEnum;
    public timeToValue: number;
    public growthRate: number;
    public effectOfIntrVal: number;
}

@Component({
    selector: 'app-security-analysis',
    template: `
        <div class="container">
            <div class="security-body">
                <div class="interact-bar">
                    <h1>buttons and search bar</h1>
                    <input #tickerInput type="text" placeholder="Enter Ticker symbol"/>
                    <button class="btn-primary" (click)="handleTickerSearch(tickerInput)">Click</button>
                </div>
                <div class="owner-summary">
                    <h2 class="text-center">Owner's Summary</h2>
                    <div class="summary-columns">
                        <div class="summary-col">
                            <span>Intrinsic Value</span>
                            <span>1 Year Growth</span>
                            <span>5 Year Growth</span>
                        </div>
                        <div class="summary-col">
                            <span>Historic Financials</span>
                            <span>Acute Financials</span>
                            <span>Projected Financials</span>
                        </div>
                        <div class="summary-col">
                            <span>Est. Time to Value:</span>
                            <span>Sustainable Growth Rate</span>
                            <span>Effect from Intrinsic Value</span>
                        </div>
                    </div>
                </div>
                <div class="security-details">
                    <div class="cashflow">
                        <h3>Discounted Cashflow</h3>
                    </div>
                    <div class="capital">
                        <h3>Captial Structure</h3>
                    </div>
                    <div class="management">
                        <h3>Management Effectiveness</h3>
                    </div>
                </div>
            </div>
        </div>
    `,
    styleUrls: ['security-analysis.component.css']
})
export class SecurityAnalysisComponent implements OnInit {

    constructor() { }

    ngOnInit() { }

    public handleTickerSearch(tickerInput: HTMLInputElement) {
        console.log(tickerInput.value);
    }
}
