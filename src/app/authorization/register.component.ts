import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgForm } from '@angular/forms';
import { AuthService } from './auth.service';
import { Subscription } from 'rxjs';

// TODO: Cleanup styling
@Component({
    selector: 'app-register',
    template: `
        <div style=" padding-top: 2rem; background-color: #6b789a; display: flex;">
        <div class="alert alert-danger" *ngIf="errorMessage">
            <p>{{ errorMessage }}</p>
        </div>
        <h1 style="width: 100%; text-align: center; color: white; background-color: #6b789a;"> Register </h1>
        </div>
        <div
            style="padding-top: 2rem; padding-left: 3rem; padding-right: 3rem;">
            <form #registrationForm="ngForm" (ngSubmit)="onSubmit(registrationForm)">
                <div class="form-group">
                    <input type="email"
                    id="email"
                    class="form-control"
                    ngModel
                    name="email"
                    required
                    email
                    placeholder="Email"
                    />
                </div>
                <div class="form-group">
                    <input type="text"
                    id="username"
                    class="form-control"
                    name="username"
                    ngModel
                    maxlength="12"
                    required
                    placeholder="Username"
                    />
                </div>
                <div class="form-group">
                    <input type="password"
                    id="password"
                    class="form-control"
                    name="password"
                    type="password"
                    ngModel
                    minlength="6"
                    required
                    placeholder="Password"
                    />
                </div>
                <div class="text-center">
                    <button
                        class="btn btn-primary btn-block"
                        type="submit"
                        [disabled]="!registrationForm.valid">
                        Register
                    </button>
                </div>
            </form>
            <h4 style="width: 100%; text-align: center;">
                Already have an account? <br /> Click
                    <a (click)="onLoginClick()" style="cursor: pointer; color: #6b789a !important;">here</a>
                to login.
            </h4>
        </div>
    `,
    styleUrls: ['login.component.css']
})
export class RegisterComponent implements OnInit, OnDestroy {
    public errorMessage: string;
    public errorSubscription: Subscription;

    constructor(
        public router: Router,
        public activatedRoute: ActivatedRoute,
        public authService: AuthService
    ) { }

    ngOnInit() {
        this.errorSubscription = this.authService.errorEmitted.subscribe((error: string) => {
            this.errorMessage = error;
        });
    }

    public onLoginClick(): void {
        this.router.navigate( ['../login'], {relativeTo: this.activatedRoute} );
    }

    public async onSubmit( form: NgForm ) {
        const email = form.value.email;
        const password = form.value.password;
        const username = form.value.username;

        await this.authService.registerUser(email, password, username);

        form.reset();
    }

    ngOnDestroy(): void {
        this.errorSubscription.unsubscribe();
    }
}
