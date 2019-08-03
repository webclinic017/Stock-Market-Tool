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
        this.http.get( this.dbUrl + 'security/info', { params }).subscribe((res) => {
            return res;
        });
    }

    // Register a new user.
    public register(registerRequest: RegisterRequest) {
        const params = new HttpParams().set('username', registerRequest.username);
        params.set('email', registerRequest.email);
        params.set('password', registerRequest.password);
        this.http.put( this.dbUrl + 'users/register', { params }).subscribe((res) => {
            return res;
        });
    }

    // Login an existing user.
    public login(loginRequest: LoginRequest) {
        const params = new HttpParams().set('username', loginRequest.username);
        params.set('password', loginRequest.password);
        this.http.put( this.dbUrl + 'users/login', { params }).subscribe((res) => {
            return res;
        });
    }

    // TODO:
    // Compute security analysis.
    public securityAnalysis(): void {
        // TODO: Call to backend.
        // return response.
    }
}
