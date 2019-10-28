import { Injectable } from '@angular/core';
import { AppEndpointService } from '../server-communication/app-endpoint.service';

@Injectable({ providedIn: 'root' })
export class SecurityAnalysisService {

    constructor(private _appEndpointService: AppEndpointService) { }


}
