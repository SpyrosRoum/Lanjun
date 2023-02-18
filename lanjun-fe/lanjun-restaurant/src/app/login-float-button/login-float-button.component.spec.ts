import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginFloatButtonComponent } from './login-float-button.component';

describe('LoginFloatButtonComponent', () => {
  let component: LoginFloatButtonComponent;
  let fixture: ComponentFixture<LoginFloatButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoginFloatButtonComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LoginFloatButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
