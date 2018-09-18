import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthorsDetailComponent } from './authors-detail.component';

describe('AuthorsDetailComponent', () => {
  let component: AuthorsDetailComponent;
  let fixture: ComponentFixture<AuthorsDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AuthorsDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AuthorsDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
