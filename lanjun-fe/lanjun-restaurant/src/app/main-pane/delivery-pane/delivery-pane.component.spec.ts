import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeliveryPaneComponent } from './delivery-pane.component';

describe('DeliveryPaneComponent', () => {
  let component: DeliveryPaneComponent;
  let fixture: ComponentFixture<DeliveryPaneComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeliveryPaneComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeliveryPaneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
