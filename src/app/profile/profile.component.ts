import { Component, OnInit, ElementRef } from '@angular/core';
import { Router } from '@angular/router';

@Component({
    selector: 'app-profile',
    template: `
        <div class="container">
            <h1>Hello, world!</h1>
        </div>
    `,
    styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
    constructor() { }

    ngOnInit(): void { }

}
