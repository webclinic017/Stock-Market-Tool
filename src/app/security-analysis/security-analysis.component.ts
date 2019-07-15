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
                    <h2 class="text-center font-weight-bold">American Express Co. (AXP) Owner's Summary</h2>
                    <div class="summary-columns">
                        <div class="summary-col">
                            <div>
                                <span style="padding-right: 2.9rem; font-weight: bold;">Intrinsic Value</span>
                                <span>{{ this.testData.intrinsicValue }}</span>
                            </div>
                            <div>
                                <span style="padding-right: 3rem; font-weight: bold;">1 Year Growth</span>
                                <span>{{ this.testData.oneYearGrowth }}</span>
                            </div>
                            <div>
                                <span style="padding-right: 3rem; font-weight: bold;">5 Year Growth</span>
                                <span>{{ this.testData.fiveYearGrowth }}</span>
                            </div>
                        </div>
                        <div class="summary-col">
                            <div>
                                <span style="padding-right: 3.89rem; font-weight: bold;">Historic Financials</span>
                                <span
                                    *ngIf="this.testData.historicFin === 0; else unhealthy"
                                    style="font-weight: bold; color: LimeGreen">
                                    {{ this.finEnum[this.testData.historicFin] }}
                                    <span class="oi oi-circle-check" style="color: LimeGreen" aria-hidden="true"></span>
                                </span>
                                <ng-template #unhealthy>
                                    <span style="font-weight: bold; color: Red">
                                        {{ this.finEnum[this.testData.historicFin] }}
                                    </span>
                                </ng-template>
                            </div>
                            <div>
                                <span style="padding-right: 5.1rem; font-weight: bold;">Acute Financials</span>
                                <span
                                    *ngIf="this.testData.acuteFin === 0; else unhealthy"
                                    style="font-weight: bold; color: LimeGreen">
                                    {{ this.finEnum[this.testData.acuteFin] }}
                                    <span class="oi oi-circle-check" style="color: LimeGreen" aria-hidden="true"></span>
                                </span>
                                <ng-template #unhealthy>
                                    <span style="font-weight: bold; color: Red">
                                        {{ this.finEnum[this.testData.acuteFin] }}
                                    </span>
                                </ng-template>
                            </div>
                            <div>
                                <span style="padding-right: 2.6rem; font-weight: bold;">Projected Financials</span>
                                <span
                                    *ngIf="this.testData.projectedFin === 0; else unhealthy"
                                    style="font-weight: bold; color: LimeGreen">
                                    {{ this.finEnum[this.testData.projectedFin] }}
                                    <span class="oi oi-circle-check" style="color: LimeGreen" aria-hidden="true"></span>
                                </span>
                                <ng-template #unhealthy>
                                    <span style="font-weight: bold; color: Red">
                                        {{ this.finEnum[this.testData.projectedFin] }}
                                        <span class="oi oi-circle-x" style="color: Red" aria-hidden="true"></span>
                                    </span>
                                </ng-template>
                            </div>
                        </div>
                        <div class="summary-col">
                            <div>
                                <span style="padding-right: 6.9rem; font-weight: bold;">Est. Time to Value</span>
                                <span>{{ this.testData.fiveYearGrowth }}</span>
                            </div>
                            <div>
                                <span style="padding-right: 2.3rem; font-weight: bold;">Sustainable Growth Rate</span>
                                <span>{{ this.testData.fiveYearGrowth }}</span>
                            </div>
                            <div>
                                <span style="padding-right: 1.6rem; font-weight: bold;">Effect from Intrinsic Value</span>
                                <span>{{ this.testData.fiveYearGrowth }}</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="security-details">
                    <div class="cashflow">
                        <h3>Discounted Cashflow</h3>
                        <div class="col-row">
                            <span>Cash and Equivalents</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Short-Term Assets</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Long-Term Assets</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Discounted Cashflow</span>
                            <span>1232</span>
                        </div>
                        <hr style="border-color: black" />
                        <div class="col-row">
                            <span>Intrinsic Value</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Price</span>
                            <span>1232</span>
                        </div>
                        <hr style="border-color: black" />
                        <div class="col-row">
                            <span>Net Margin of Safety</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Margin of Safety</span>
                            <span>1232</span>
                        </div>
                    </div>
                    <div class="capital">
                        <h3 align="center">Capital Structure</h3>
                        <h4 align="center" style="color: orange">Moderate Leverage</h4>
                        <div class="col-row">
                            <span>Debt-to-Capital-Ratio</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Debt-to-Equity-Ratio <br> (D/E)</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Interest Coverage <br> Ratio</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Degree of Combined <br> Leverage</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Degree of Operating <br> Leverage (DOL)</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Degree of Financial <br> Leverage</span>
                            <span>1232</span>
                        </div>
                    </div>
                    <div class="management">
                        <h3>Management Effectiveness</h3>
                        <div class="col-row">
                            <span>Price to Earnings Ration (P/E)</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Earning Yield (E/P)</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Absolue P/E</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Relative P/E</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Return on Equity (ROE)</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Return on Invested Capital (ROIC)</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Retention Ratio</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Sustainable Growth Rate</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Return on Assets (ROA)</span>
                            <span>1232</span>
                        </div>
                        <div class="col-row">
                            <span>Price to Book (P/B)</span>
                            <span>1232</span>
                        </div>
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

    ngOnInit() { }

    public async handleTickerSearch(tickerInput: HTMLInputElement): Promise<void> {
        // TODO: Set display to load.
        const ticker = tickerInput.value;
        // this.testData = await this._endpointService.securityAnalysis(ticker);
        // TODO: End loading, display details.
    }
}
