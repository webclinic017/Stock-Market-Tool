import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../authorization/auth.service';
import { ToastrService } from 'ngx-toastr';

@Component({
    selector: 'app-profile',
    template: `
        <div class="container profile-body">
            <div class="profile-row">
                <div class="profile-component">
                    <div class="portfolio">
                        <h1>Hi</h1>
                    </div>
                </div>
                <div *ngIf="tickerIsLoaded" class="profile-component">
                    <div class="table">
                    </div>
                </div>
            </div>
            <div class="profile-row">
                <div>
                    <button
                        (click)="handleLogoutClick()"
                        class="btn btn-info">Logout
                    </button>
                </div>
                <div *ngIf="tickerIsLoaded" class="profile-component">
                    <div class="">
                    </div>
                </div>
            </div>
        </div>
    `,
    styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
    public tickerIsLoaded = false;

    constructor(
        public router: Router,
        public authService: AuthService,
        private _toastrService: ToastrService
    ) { }

    ngOnInit(): void { }

    public handleLogoutClick(): void {
        this.authService.isLoggedIn.next(false);
        this._toastrService.success('Logout successful');
        this.router.navigate(['home']);
    }
}
