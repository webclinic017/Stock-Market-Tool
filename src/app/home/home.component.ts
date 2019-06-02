import { Component, OnInit, ElementRef } from '@angular/core';

@Component({
  selector: 'app-home',
  template: `
  <div>
    <h1> uh </h1>
  </div>
  `,
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private elementRef: ElementRef) { }

  ngOnInit() {
    this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = 'aqua';
  }
}
