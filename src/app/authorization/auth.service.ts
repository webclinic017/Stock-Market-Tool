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
    public async registerUser(username: string, email: string, password: string): Promise<void> {
        try {
            const response = await this.endpointService.register({email, password, username});
        } catch (error) {
            console.log(error.error.error.message);
        }
    }

    // Recieve user login credentials from backend.
    public async login(username: string, password: string): Promise<void> {
        try {
            const response = await this.endpointService.login({username, password});
        } catch (error) {
            console.log(error.error.message);
        }
    }
}
