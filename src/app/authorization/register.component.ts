import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgForm } from '@angular/forms';

@Component({
    selector: 'app-register',
    template: `
        <form #registrationForm="ngForm" (ngSubmit)="onSubmit(registrationForm)">
            <div class="form-group">
                <label for="email">E-Mail</label>
                <input type="email"
                id="email"
                class="form-control"
                ngModel
                name="email"
                required
                email
                />
            </div>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text"
                id="username"
                class="form-control"
                name="username"
                ngModel
                maxlength="12"
                required
                />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password"
                id="password"
                class="form-control"
                name="password"
                ngModel
                minlength="6"
                required
                />
            </div>
            <div>
                <button
                    class="btn btn-primary"
                    type="submit"
                    [disabled]="!registrationForm.valid">
                    Sign Up
                </button>
                <h4>
                    Already have an account? Click
                        <a (click)="onLoginClick()" style="cursor: pointer;">here</a>
                    to login.
                </h4>
            </div>
        </form>
    `,
    styleUrls: ['login.component.css']
})
export class RegisterComponent implements OnInit {

    constructor( public router: Router, public activatedRoute: ActivatedRoute ) { }

    ngOnInit() { }

    onLoginClick(): void {
        this.router.navigate( ['../login'], {relativeTo: this.activatedRoute} );
    }

    onSubmit( form: NgForm ): void {
        console.log(form.value);
        form.reset();
    }
}
