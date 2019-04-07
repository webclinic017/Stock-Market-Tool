import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BuyRecListComponent } from './buy-rec-list.component';

describe('BuyRecListComponent', () => {
  let component: BuyRecListComponent;
  let fixture: ComponentFixture<BuyRecListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BuyRecListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BuyRecListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
