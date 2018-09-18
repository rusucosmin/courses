import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthorsNewComponent } from './authors-new.component';

describe('AuthorsNewComponent', () => {
  let component: AuthorsNewComponent;
  let fixture: ComponentFixture<AuthorsNewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AuthorsNewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AuthorsNewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
