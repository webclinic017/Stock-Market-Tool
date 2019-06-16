import { Component } from '@angular/core';

// TODO: Change Login to be included in the component, not root.
@Component({
    selector: 'app-auth',
    template: `
    <body style="margin-top: -2rem;">
        <div class="col-xs-3 col-xs-offset-4"
            style="margin-top: 10rem; padding-top: 2rem;
                padding-left: 3rem; padding-right: 3rem; background-color: #6b789a;">
            <h1 style="color: white;">Login</h1>
        </div>
        <div class="col-xs-3 col-xs-offset-4" style="padding-top: 2rem; padding-left: 3rem; padding-right: 3rem;">
            <router-outlet></router-outlet>
        </div>
    </body>
    `,
    styleUrls: ['auth.component.css']
})
export class AuthComponent {

}
