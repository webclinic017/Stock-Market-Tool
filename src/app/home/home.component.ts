import { Component, OnInit, ElementRef } from '@angular/core';
import { Router } from '@angular/router';

@Component({
    selector: 'app-home',
    template: `
        <div class="container fill-height" style="margin-top: 13rem;">
            <div class="row">
                <div class="col-lg-1"></div>
                    <div class="col-lg-10 text-center">
                        <h1>
                            A Sensible Approach to Financial
                        </h1>
                        <h1 class="big_font_120">SUCCESS</h1>
                        <button
                            type="button"
                            class="btn btn-primary"
                            (click)="onStartNow()">
                            Start Now
                        </button>
                    </div>
            </div>
        </div>
    `,
    styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
    constructor(
        private elementRef: ElementRef,
        private router: Router
    ) { }

    ngOnInit() { }

    // Route to Market Analysis.
    public onStartNow() {
        console.log('redirect to Market Analysis tab');
        this.router.navigate(['market-analysis']);
    }
}
