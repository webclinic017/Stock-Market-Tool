import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { RegisterRequest, LoginRequest, SecuritysRequest, LoginResponse, RegisterResponse, ReportedRequest, ReportedResponse } from './app-endpoint.constants';

@Injectable({ providedIn: 'root' })
export class AppEndpointService {
    private _dbUrl = 'http://localhost:3000/api/';

    constructor(private http: HttpClient) { }

    /*public getSecurity(securitysRequest: SecuritysRequest) {
        const params = new HttpParams().set('ticker', securitysRequest.ticker);
        return this.http.get(`${this._dbUrl}security/info`, { params }).toPromise();
    }*/

    public getReported(reportedRequest: ReportedRequest): Promise<ReportedResponse> {
        return this.http.post<ReportedResponse>(`${this._dbUrl}security/getReportedTicker`, reportedRequest).toPromise();
    }

    public register(registerRequest: RegisterRequest): Promise<RegisterResponse>  {
        return this.http.post<RegisterResponse>(`${this._dbUrl}user/register`, registerRequest).toPromise();
    }

    public login(loginRequest: LoginRequest): Promise<LoginResponse> {
        return this.http.post<LoginResponse>(`${this._dbUrl}user/login`, loginRequest).toPromise();
    }

    public getWatchList(getWatchlistRequest) {
        return this.http.post(`${this._dbUrl}user/getWatchlist`, getWatchlistRequest).toPromise();
    }

    public addWatchlistTicker(addWatchlistTickerRequest) {
        return this.http.post(`${this._dbUrl}user/addWatchlistTicker`, addWatchlistTickerRequest).toPromise();
    }

    public securityAnalysis(): void {
        // TODO: Call to backend.
        // return response.
    }
}
