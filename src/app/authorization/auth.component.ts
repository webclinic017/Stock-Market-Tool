import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { AuthService } from './auth.service';

// TODO: Cleanup styling
@Component({
    selector: 'app-auth',
    template: `
    <body>
            <div>
            <router-outlet></router-outlet>
            </div>
    </body>
    `,
    styleUrls: ['auth.component.css']
})
export class AuthComponent implements OnInit, OnDestroy {

    constructor(public authService: AuthService) { }

    ngOnInit(): void { }

    ngOnDestroy(): void { }
}
