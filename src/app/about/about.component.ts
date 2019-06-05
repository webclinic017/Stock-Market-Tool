import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-about',
    template: `
        <div class="row">
            <div class="col-xs-10">
                <h1>about Component</h1>
            </div>
        </div>
    `,
})
export class AboutComponent implements OnInit {

    ngOnInit() {}

}
