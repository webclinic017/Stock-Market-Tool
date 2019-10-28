import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../authorization/auth.service';
import { ToastrService } from 'ngx-toastr';
import { ProfileService } from './profile.service';

@Component({
    selector: 'app-profile',
    template: `
        <div *ngIf="!pageIsLoading" class="container profile-body">
            <div class="profile-row">
                <div class="profile-component">
                    <div class="portfolio">
                        <div class="profile-component-header">
                            <span style="font-size: 6rem;">Watchlist</span>
                        </div>
                        <div *ngFor="let item of watchlist;" class="watchlist-item">
                                {{item.ticker}}
                        </div>
                    </div>
                </div>
                <div *ngIf="tickerIsLoaded" class="profile-component">
                    <div class="profile-component-header">
                        <span>Watchlist</span>
                    </div>
                    <div *ngFor="let item of watchlist;">
                        <span>
                            {{item.ticker}}
                        </span>
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
        <div *ngIf="pageIsLoading" class="center-spinner">
            <div class="lds-dual-ring lds-margin-top"></div>
        </div>
    `,
    styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
    public tickerIsLoaded = false;
    public pageIsLoading: boolean;
    public watchlist;

    constructor(
        public router: Router,
        public authService: AuthService,
        public profileService: ProfileService,
        private _toastrService: ToastrService
    ) { }

    async ngOnInit() {
        this.pageIsLoading = true;
        this.watchlist = await this.profileService.listWatchlist();
        this.pageIsLoading = false;
        console.log(this.watchlist[0]);
    }

    public handleLogoutClick(): void {
        this.authService.isLoggedIn.next(false);
        this._toastrService.success('Logout successful');
        this.router.navigate(['home']);
    }
}

/*
dateAdded: "2019-09-28T04:00:00.000Z"
priceEntered: 94.99
ticker: "KMX"
_id: "5db726cc74361f39a50163d7"
*/
