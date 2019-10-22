import { Component, OnInit } from '@angular/core';
import { AppEndpointService } from '../../server-communication/app-endpoint.service';

@Component({
    selector: 'app-reported',
    template: `
        <app-income-statement-table><app-income-statement-table>
    `,
    styleUrls: ['reported.component.scss']
})
export class ReportedComponent implements OnInit {
    constructor(private _appEndpointService: AppEndpointService) { }

    async ngOnInit() {
        const res = await this._appEndpointService.getReported({ticker: 'HRB'});
        console.log(res);
    }
}
