import { Component, OnInit } from '@angular/core';
import { AppEndpointService } from '../app-endpoint.service';

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
    public ticker: string;
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

// TODO: Ticker enum that displays as follows:
// AXP : 0, then in display enum 'American express Co. (AXP)'
// export class tickerEnum {} export class tickerDisplayEnum

@Component({
    selector: 'app-security-analysis',
    template: `
        <div class="container">
            <div class="security-body">
                <div class="interact-bar">
                    <div>
                        <input #tickerInput type="text" placeholder="Enter Ticker symbol"/>
                        <button class="btn-primary" (click)="handleTickerSearch(tickerInput)">Search</button>
                    </div>
                    <div>
                        <button class="btn-primary">ML Model</button>
                        <button class="btn-primary">Reported</button>
                        <button class="btn-primary">Per Share</button>
                        <button class="btn-primary">Per Dollar</button>
                    </div>
                </div>
                <!-- TODO: Change to more simple table on small screen/mobile -->
                <div class="owner-summary">
                    <h2 class="text-center">American Express Co. (AXP) Owner's Summary</h2>
                    <div class="summary-columns">
                        <div class="summary-col">
                            <div>
                                <span style="padding-right: 3.2rem;">Intrinsic Value</span>
                                <span>{{ this.testData.intrinsicValue }}</span>
                            </div>
                            <div>
                                <span style="padding-right: 3rem;">1 Year Growth</span>
                                <span>{{ this.testData.oneYearGrowth }}</span>
                            </div>
                            <div>
                                <span style="padding-right: 3rem;">5 Year Growth</span>
                                <span>{{ this.testData.fiveYearGrowth }}</span>
                            </div>
                        </div>
                        <div class="summary-col">
                            <div>
                                <span style="padding-right: 4.2rem;">Historic Financials</span>
                                <span
                                    [ngStyle]="{'color': this.testData.historicFin === 0 ? 'LimeGreen' : 'Red'}"
                                    style="font-weight: bold;">{{ this.finEnum[this.testData.historicFin] }}
                                </span>
                            </div>
                            <div>
                                <span style="padding-right: 5.4rem;">Acute Financials</span>
                                <span
                                    [ngStyle]="{'color': this.testData.acuteFin === 0 ? 'LimeGreen' : 'Red'}"
                                    style="font-weight: bold;">{{ this.finEnum[this.testData.acuteFin] }}
                                </span>
                            </div>
                            <div>
                                <span style="padding-right: 3rem;">Projected Financials</span>
                                <span
                                    [ngStyle]="{'color': this.testData.projectedFin === 0 ? 'LimeGreen' : 'Red'}"
                                    style="font-weight: bold;">{{ this.finEnum[this.testData.projectedFin] }}
                                </span>
                            </div>
                        </div>
                        <div class="summary-col">
                            <div>
                                <span style="padding-right: 6.9rem;">Est. Time to Value</span>
                                <span>{{ this.testData.fiveYearGrowth }}</span>
                            </div>
                            <div>
                                <span style="padding-right: 2.6rem;">Sustainable Growth Rate</span>
                                <span>{{ this.testData.fiveYearGrowth }}</span>
                            </div>
                            <div>
                                <span style="padding-right: 2.3rem;">Effect from Intrinsic Value</span>
                                <span>{{ this.testData.fiveYearGrowth }}</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="security-details">
                    <div class="cashflow">
                        <h3 class="cashflow-header">Discounted Cashflow</h3>
                    </div>
                    <div class="capital">
                        <h3 class="cashflow-header">Captial Structure</h3>
                    </div>
                    <div class="management">
                        <h3 class="cashflow-header">Management Effectiveness</h3>
                    </div>
                </div>
            </div>
        </div>
    `,
    styleUrls: ['security-analysis.component.css']
})
export class SecurityAnalysisComponent implements OnInit {
    public testData: OwnerSummary = {
        ticker: 'AXP',
        intrinsicValue: 1212,
        oneYearGrowth: 12121,
        fiveYearGrowth: 1212,
        historicFin: 0,
        acuteFin: 0,
        projectedFin: 1,
        timeToValue: 1,
        growthRate: 12,
        effectOfIntrVal: 1211
    };
    public finEnum = FinancialsDisplayEnum;

    constructor(
        private _endpointService: AppEndpointService
    ) { }

    ngOnInit() {
        // TODO:
    }

    public async handleTickerSearch(tickerInput: HTMLInputElement): Promise<void> {
        // TODO: Set display to load.
        const ticker = tickerInput.value;
        // this.testData = await this._endpointService.securityAnalysis(ticker);
        // TODO: End loading, display details.
    }
}
