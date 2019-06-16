import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { AuthService } from './auth.service';

// TODO: Cleanup styling
@Component({
    selector: 'app-auth',
    template: `
    <body style="margin-top: -10rem; ">
            <div style="
            position:relative;
            top:25%;
            margin: auto;
            width: 30%;
            height: 40%;
            -webkit-box-shadow: 0 0 100px 100px black;">
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
