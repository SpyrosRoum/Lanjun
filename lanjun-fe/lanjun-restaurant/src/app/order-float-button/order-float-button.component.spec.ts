import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrderFloatButtonComponent } from './order-float-button.component';

describe('OrderFloatButtonComponent', () => {
  let component: OrderFloatButtonComponent;
  let fixture: ComponentFixture<OrderFloatButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OrderFloatButtonComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OrderFloatButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
