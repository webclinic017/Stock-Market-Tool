import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgForm } from '@angular/forms';
import { formArrayNameProvider } from '@angular/forms/src/directives/reactive_directives/form_group_name';
import { AuthService } from './auth.service';

// TODO: Cleanup styling
@Component({
    selector: 'app-login',
    template: `
        <div style=" padding-top: 2rem; background-color: #6b789a; display: flex;">
            <h1 style="width: 100%; text-align: center; color: white; background-color: #6b789a;"> Login </h1>
        </div>
        <div
            style="padding-top: 2rem; padding-left: 3rem; padding-right: 3rem;">
            <form #registrationForm="ngForm" (ngSubmit)="onSubmit(registrationForm)">
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
                        Login
                    </button>
                    <h4>
                        Don't have an account? <br /> Click
                            <a (click)="onRegisterClick()" style="cursor: pointer; color: #6b789a !important;">here</a>
                        to register.
                    </h4>
                </div>
            </form>
        </div>
    `,
    styleUrls: ['login.component.css']
})
export class LoginComponent implements OnInit {

    constructor(
        public router: Router,
        public activatedRoute: ActivatedRoute,
        public authService: AuthService
    ) { }

    ngOnInit() { }

    public onRegisterClick(): void {
        this.router.navigate( ['../register'], {relativeTo: this.activatedRoute} );
    }

    public onSubmit( form: NgForm ): void {
        console.log(form.value);
        form.reset();
    }
}
