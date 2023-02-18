import { EventEmitter, Injectable, Output } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SwapperService {
  private panel: string;
  static panelSubject: Subject<string> = new Subject();

  constructor() {
    this.panel = 'reservation';
  }

  getPanel(): string {
    return this.panel;
  }

  setPanel(panel: string) {
    this.panel = panel;
    SwapperService.panelSubject.next(panel);
  }
}
