import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription, Subject } from 'rxjs';
import { AuthService } from './auth.service';
import { device } from 'device.js';

@Component({
    selector: 'app-auth',
    template: `
    <body *ngIf="isLoginView; else registerView" class="auth-body">
        <div *ngIf="!isMobile; else mobileView" class="desktop-auth-login">
            <router-outlet></router-outlet>
        </div>
        <ng-template #mobileView>
            <div class="mobile-auth-login">
                <router-outlet></router-outlet>
            </div>
        </ng-template>
    </body>
    <ng-template #registerView>
        <body class="auth-body">
            <div *ngIf="!isMobile; else mobileView" class="desktop-auth-register">
                <router-outlet></router-outlet>
            </div>
            <ng-template #mobileView>
                <div class="mobile-auth-register">
                    <router-outlet></router-outlet>
                </div>
            </ng-template>
        </body>
    </ng-template>
    `,
    styleUrls: ['auth.component.css']
})
export class AuthComponent implements OnInit, OnDestroy {
    public isMobile: boolean;
    public isLoginView = true;
    public viewChangeSubscription: Subscription;

    constructor(public authService: AuthService) { }

    ngOnInit(): void {
        // Set view according to device type.
        device.addClasses(document.documentElement);
        this.isMobile = device.mobile;

        // Toggle size of window bases on register or login view.
        this.viewChangeSubscription = this.authService.viewChanged.subscribe(() => {
            this.isLoginView = !this.isLoginView;
        });
    }

    ngOnDestroy(): void { }
}
