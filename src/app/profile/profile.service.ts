import { Injectable } from '@angular/core';
import { AppEndpointService } from '../server-communication/app-endpoint.service';
import { AuthService } from '../authorization/auth.service';

@Injectable({ providedIn: 'root' })
export class ProfileService {
    public loggedInUser: string;

    constructor(
        public appEndpointService: AppEndpointService,
        public authService: AuthService
    ) {
        this.loggedInUser = this.authService.loggedInUser;
    }

    listWatchlist() {
        return this.appEndpointService.getWatchList({username: this.loggedInUser});
    }
}
