import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FundFormulaComponent } from './fund-formula.component';

describe('FundFormulaComponent', () => {
  let component: FundFormulaComponent;
  let fixture: ComponentFixture<FundFormulaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FundFormulaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FundFormulaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
