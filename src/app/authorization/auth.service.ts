import { Subject } from 'rxjs';
import { Injectable } from '@angular/core';
import { AppEndpointService } from '../server-communication/app-endpoint.service';

@Injectable({ providedIn: 'root' })
export class AuthService {
    public error: string;
    public errorEmitted = new Subject<string>();
    public currentView = new Subject<string>();

    constructor(public endpointService: AppEndpointService) { }

    // Register user with backend.
    public async registerUser(username: string, email: string, password: string) {
        const response = await this.endpointService.register({email, password, username});
    }

    // Recieve user login credentials from backend.
    public async login(username: string, password: string) {
        const response = await this.endpointService.login({username, password});
    }
}
