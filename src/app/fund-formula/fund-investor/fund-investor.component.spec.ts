import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FundInvestorComponent } from './fund-investor.component';

describe('FundInvestorComponent', () => {
  let component: FundInvestorComponent;
  let fixture: ComponentFixture<FundInvestorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FundInvestorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FundInvestorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
