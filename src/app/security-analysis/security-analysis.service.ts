import { Injectable } from '@angular/core';
import { AppEndpointService } from '../server-communication/app-endpoint.service';
import { GetScoreCardResponse, GetScoreCardRequest } from '../server-communication/app-endpoint.constants';

@Injectable({ providedIn: 'root' })
export class SecurityAnalysisService {

    constructor(private _appEndpointService: AppEndpointService) { }

    public async getScorecards(getScoreCardRequest: GetScoreCardRequest): Promise<GetScoreCardResponse> {
        return await this._appEndpointService.getScoreCard(getScoreCardRequest);
    }

}
