import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AboutPaneComponent } from './about-pane.component';

describe('AboutPaneComponent', () => {
  let component: AboutPaneComponent;
  let fixture: ComponentFixture<AboutPaneComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AboutPaneComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AboutPaneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
