import { Component } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { ApiService } from "./ApiService";

@Component({
  selector: "tv-q",
  templateUrl: "TVQuestion.html"
})
export class TVQuestionComponent {
  public localsite = "http://localhost:4200/";
  counter = 0;

  timer = setInterval(this.next, 1000);

  next() {
    this.counter += 1;
    if (this.counter == 8) {
      window.location.href = this.localsite + "products";
    }
  }

  back() {
    if (this.counter < 2) {
      console.log("beginning of qs");
    } else this.counter -= 1;
  }
}
