import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BuyRecComponent } from './buy-rec.component';

describe('BuyRecComponent', () => {
  let component: BuyRecComponent;
  let fixture: ComponentFixture<BuyRecComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BuyRecComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BuyRecComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
