import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReservationPaneComponent } from './reservation-pane.component';

describe('ReservationPaneComponent', () => {
  let component: ReservationPaneComponent;
  let fixture: ComponentFixture<ReservationPaneComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReservationPaneComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ReservationPaneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
