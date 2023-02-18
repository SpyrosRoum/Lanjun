import { Component, OnInit } from '@angular/core';
import { SwapperService } from '../swapper.service';

@Component({
  selector: 'app-side-bar',
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.css'],
  providers: [SwapperService]
})
export class SideBarComponent implements OnInit {

  public open_hours: string;

  weekdays: Array<string> = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];

  months: Array<string> = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];


  constructor(private swapperService: SwapperService) {
    let date = new Date();
    let hour: number = date.getHours();
    let hourString: string = hour > 9 ? hour + "" : "0" + hour;
    let mins: number = date.getMinutes();
    let minutesString: string = mins > 9 ? mins + "" : "0" + mins;
    let dayWeek: number = date.getDay();
    this.open_hours = "It's " + this.weekdays[dayWeek] + ", ";

    this.open_hours = this.open_hours + " " + hourString + ":" + minutesString;

    this.isOpen(hour, dayWeek);
  }

  ngOnInit(): void {
  }

  isOpen(time: number, dayweek: number): void {
    if (time > 14 && time <= 24 && dayweek != 0)
      this.open_hours += " and we are open!";
    else
      this.open_hours += " so we are closed...";
  }

  swapper(panel: string): void {
    this.swapperService.setPanel(panel);
  }
}
