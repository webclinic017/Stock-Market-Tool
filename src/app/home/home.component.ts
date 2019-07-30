import { Component, OnInit, ElementRef } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-home',
    template: `
        <div class="bg">
            <div style="margin-top: -2rem;">
                <div class="home-content">
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
        private router: Router,
        private http: HttpClient
    ) { }

    ngOnInit() { }

    // Route to Market Analysis.
    public onStartNow() {
        /*
        console.log('redirect to Market Analysis tab');
        this.router.navigate(['market-analysis']);
        */
        this.http.get('api/security/info').subscribe((res) => {
            console.log(res);
        });
    }
}
