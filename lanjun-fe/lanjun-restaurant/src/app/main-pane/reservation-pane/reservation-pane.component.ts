import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Reservation } from 'src/app/reservation.model';

@Component({
  selector: 'app-reservation-pane',
  templateUrl: './reservation-pane.component.html',
  styleUrls: ['./reservation-pane.component.css']
})
export class ReservationPaneComponent implements OnInit {
  @Output() reservation: EventEmitter<Reservation> = new EventEmitter<Reservation>();
  public reserved: boolean;
  public people: string;
  public date: string;
  constructor() {
    this.reserved = false;
    this.people = "";
    this.date = "";
  }

  ngOnInit(): void {
  }

  reserve(form: NgForm) {

    if (form.value.date && form.value.people) {
      let res: Reservation = new Reservation();
      res.date = form.value.date;
      res.people = +form.value.people;
      this.reservation.emit(res);
      this.reserved = true;
      this.people = res.people + " " + ((+res.people > 1) ? "people" : "person");
      this.date = form.value.date;
      
      form.resetForm();
    }

    return false;
  }
}
