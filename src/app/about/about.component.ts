import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-about',
    template: `
        <div class="row">
            <div class="col-md-5 text-center">
                <h1>bottom text</h1>
            </div>
            <div class="col-md-7">
                <h3>yup</h3>
            </div>
        </div>
    `,
})
export class AboutComponent implements OnInit {

    ngOnInit() {}

}
