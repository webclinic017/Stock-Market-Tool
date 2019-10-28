import { Component, OnInit } from '@angular/core';
import { AppEndpointService } from '../server-communication/app-endpoint.service';
import { device } from 'device.js';
import { trigger, transition, style, animate, state } from '@angular/animations';
import { ReportedResponse } from '../server-communication/app-endpoint.constants';
import { ReportedService } from './reported/reported.service';

/*export enum FinancialsDisplayEnum {
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
*/
@Component({
    selector: 'app-security-analysis',
    templateUrl: 'security-analysis.component.html',
    styleUrls: ['security-analysis.component.scss'],
    animations: [
        trigger('expandAppear', [
            transition(':enter', [
                style({transform: 'scale(0)'}),
                animate('200ms ease-in', style({transform: 'scale(1)'}))
            ])
        ]),
        trigger('slideUp', [
            transition(':enter', [
                style({transform: 'translateY(100%)'}),
                animate('300ms ease-in', style({transform: 'translateY(0%)'}))
            ]),
        ]),
    ]
})
export class SecurityAnalysisComponent implements OnInit {
    /*public testData: OwnerSummary = {
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
    };*/
    // public finEnum = FinancialsDisplayEnum;

    // Booleans.
    public isMobile: boolean;
    public isLoading = false;
    public shouldShowOwnerSummary = false;

    // Display strings.
    public loadedComponent = 'dashboard';
    public reportedTickerName: string;

    // API data.
    public reportedData;

    constructor(
        private _endpointService: AppEndpointService,
        public reportedService: ReportedService
    ) { }

    ngOnInit() {
        // Set view according to device type.
        device.addClasses(document.documentElement);
        this.isMobile = device.mobile;
    }

    public async handleTickerSearch(tickerInput: HTMLInputElement): Promise<void> {
        this.isLoading = true;
        this.shouldShowOwnerSummary = false;

        const ticker = tickerInput.value;
        this.reportedData = await this._endpointService.getReported({ticker: ticker});
        console.log(this.reportedData);

        this.reportedTickerName = tickerInput.value;
        this.shouldShowOwnerSummary = true;
        this.isLoading = false;
    }

    public handleComponentClick(securityComponent: string): void {
        this.loadedComponent = securityComponent;
    }

    public handleAddWatchlistClick() {
        this.reportedService.addTickerToWatchlist(this.reportedTickerName);
    }
}
