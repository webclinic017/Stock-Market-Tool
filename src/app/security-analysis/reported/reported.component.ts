import { Component, OnInit } from '@angular/core';
import { AppEndpointService } from '../../server-communication/app-endpoint.service';
import { ReportedService } from './reported.service';

@Component({
    selector: 'app-reported',
    template: `
        <app-income-statement-table><app-income-statement-table>
        <!-- TODO: balance sheet, cashflow sheet -->
    `,
    styleUrls: ['reported.component.scss']
})
export class ReportedComponent implements OnInit {
    constructor(
        public reportedService: ReportedService,
        private _appEndpointService: AppEndpointService
    ) { }

    async ngOnInit() {
        const res = await this._appEndpointService.getReported({ticker: 'HRB'});
        console.log(res);
        await this.reportedService.getReportedData();
        this.reportedService.getIncomeTables();
    }
}
