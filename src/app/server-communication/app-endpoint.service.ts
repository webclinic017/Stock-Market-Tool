import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { RegisterRequest, LoginRequest, SecuritysRequest, LoginResponse, RegisterResponse } from './app-endpoint.constants';

@Injectable({ providedIn: 'root' })
export class AppEndpointService {
    private _dbUrl = 'http://localhost:3000/api/';

    constructor(private http: HttpClient) { }

    public getSecurity(securitysRequest: SecuritysRequest) { // TODO: Add response type.
        const params = new HttpParams().set('ticker', securitysRequest.ticker);
        return this.http.get(`${this._dbUrl}security/info`, { params }).toPromise();
    }

    public register(registerRequest: RegisterRequest): Promise<RegisterResponse>  {
        return this.http.post<RegisterResponse>(`${this._dbUrl}user/register`, registerRequest).toPromise();
    }

    public login(loginRequest: LoginRequest): Promise<LoginResponse> {
        return this.http.post<LoginResponse>(`${this._dbUrl}user/login`, loginRequest).toPromise();
    }

    // TODO: Need details from Jimmy.
    // Compute security analysis.
    public securityAnalysis(): void {
        // TODO: Call to backend.
        // return response.
    }
}
