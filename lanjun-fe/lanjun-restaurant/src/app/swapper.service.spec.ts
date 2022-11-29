import { TestBed } from '@angular/core/testing';

import { SwapperService } from './swapper.service';

describe('SwapperService', () => {
  let service: SwapperService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SwapperService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
