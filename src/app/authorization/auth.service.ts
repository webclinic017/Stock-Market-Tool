import { Subject } from 'rxjs';
import { Injectable } from '@angular/core';
import { AppEndpointService } from '../server-communication/app-endpoint.service';

@Injectable({ providedIn: 'root' })
export class AuthService {
    public currentView = new Subject<string>();
    public loginToast = new Subject<boolean>();
    public registerToast = new Subject<boolean>();
    public error = new Subject<string>();

    constructor(public endpointService: AppEndpointService) { }

    // Register user with backend.
    public async registerUser(username: string, email: string, password: string): Promise<void> {
        try {
            const response = await this.endpointService.register({email, password, username});
            this.registerToast.next(true);
        } catch (error) {
            this.error.next(error.error.error.message);
            this.registerToast.next(false);
        }
    }

    // Recieve user login credentials from backend.
    public async login(username: string, password: string): Promise<void> {
        try {
            const response = await this.endpointService.login({username, password});
            this.loginToast.next(true);
        } catch (error) {
            this.error.next(error.error.message);
            this.loginToast.next(false);
        }
    }
}
