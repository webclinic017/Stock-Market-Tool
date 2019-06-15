import { Component } from '@angular/core';

@Component({
    selector: 'app-auth',
    template: `
    <body style="margin-top: -2rem;">
        <div class="col-xs-3 col-xs-offset-4" style="margin-top: 10rem;">
            <router-outlet></router-outlet>
        </div>
    </body>
    `,
    styleUrls: ['auth.component.css']
})
export class AuthComponent {

}
