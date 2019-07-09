import { Subject } from 'rxjs';
import { Injectable } from '@angular/core';
import { AppEndpointService, RegisterResponse } from '../app-endpoint.service';

@Injectable({ providedIn: 'root' })
export class AuthService {
    public error: string;
    public errorEmitted = new Subject<string>();
    public currentView = new Subject<string>();

    constructor(public endpointService: AppEndpointService) { }

    // Register user with backend.
    public async registerUser(email: string, password: string, username: string) {
        console.log(email, password, username);

        this.endpointService.register(email, password, username).subscribe(res => {
            console.log(res);
        },
        errorMessage => {
            console.log(errorMessage);
            this.errorEmitted.next(errorMessage);
        });
    }

    // Recieve user login credentials from backend.
    public login(email: string, password: string, username: string): string {
        console.log(email, password, username);
        return '';
    }
}
