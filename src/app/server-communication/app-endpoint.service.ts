import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { RegisterRequest, LoginRequest, SecuritysRequest } from './app-endpoint.constants';

@Injectable({ providedIn: 'root' })
export class AppEndpointService {
    private dbUrl = 'http://localhost:3000/api/';

    constructor(private http: HttpClient) { }

    // Return details of security.
    public getSecurity(securitysRequest: SecuritysRequest) {
        const params = new HttpParams().set('ticker', securitysRequest.ticker);
        this.http.get(`${this.dbUrl}security/info`, { params }).subscribe((res) => {
            return res;
        });
    }

    // Register a new user.
    public register(registerRequest: RegisterRequest) {
        return this.http.post(`${this.dbUrl}user/register`, registerRequest).toPromise();
    }

    // Login an existing user.
    public async login(loginRequest: LoginRequest) {
        return this.http.post(`${this.dbUrl}user/login`, /*{ params }*/ loginRequest).toPromise();
    }

    // TODO: Need details from Jimmy.
    // Compute security analysis.
    public securityAnalysis(): void {
        // TODO: Call to backend.
        // return response.
    }
}
