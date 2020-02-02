import { Component } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { ApiService } from "./ApiService";

@Component({
  selector: "app-root",
  templateUrl: "landing.html"
})
export class LandingComponent {
  public localsite = "http://localhost:4200/";
  helpState: boolean = false;
  tv_url: string = "#"

  // toggle help on and off
  toggleHelp() {
    if (this.helpState == false) {
      this.helpState = true;
      this.tv_url = this.localsite + "tv_question"
    } else {
      this.helpState = false;
      this.tv_url = "#"
    }
  }

  // show or hide content based on helpState
  showContentToggle() {
    if (this.helpState == true) {
      return false;
    } else {
      return true;
    }
  }
}
