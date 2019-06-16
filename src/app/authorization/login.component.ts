import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgForm } from '@angular/forms';
import { formArrayNameProvider } from '@angular/forms/src/directives/reactive_directives/form_group_name';

@Component({
    selector: 'app-login',
    template: `
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
                    class="btn btn-primary"
                    style="padding-left: 17rem; padding-right: 17rem;"
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
    `,
    styleUrls: ['login.component.css']
})
export class LoginComponent implements OnInit {

    constructor( public router: Router, public activatedRoute: ActivatedRoute ) { }

    ngOnInit() { }

    onRegisterClick(): void {
        this.router.navigate( ['../register'], {relativeTo: this.activatedRoute} );
    }

    onSubmit( form: NgForm ): void {
        console.log(form.value);
        form.reset();
    }
}
