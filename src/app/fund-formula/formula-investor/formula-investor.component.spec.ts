import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FormulaInvestorComponent } from './formula-investor.component';

describe('FormulaInvestorComponent', () => {
  let component: FormulaInvestorComponent;
  let fixture: ComponentFixture<FormulaInvestorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FormulaInvestorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FormulaInvestorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
