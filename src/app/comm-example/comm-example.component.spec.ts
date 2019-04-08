import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CommExampleComponent } from './comm-example.component';

describe('CommExampleComponent', () => {
  let component: CommExampleComponent;
  let fixture: ComponentFixture<CommExampleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CommExampleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CommExampleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
