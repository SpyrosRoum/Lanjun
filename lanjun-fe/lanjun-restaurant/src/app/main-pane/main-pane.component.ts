import { Component, OnInit } from '@angular/core';
import { SwapperService } from '../swapper.service';

@Component({
  selector: 'app-main-pane',
  templateUrl: './main-pane.component.html',
  styleUrls: ['./main-pane.component.css'],
  providers: [SwapperService]
})
export class MainPaneComponent implements OnInit {
  public panel: string;

  constructor(private swapperService: SwapperService) {
    this.panel = swapperService.getPanel();

    SwapperService.panelSubject.subscribe(p => {
      this.panel = p;
    })
  }

  ngOnInit(): void {
  }

}
