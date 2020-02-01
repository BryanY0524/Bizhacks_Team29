import { Component } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { ApiService } from "./ApiService";

@Component({
  selector: "app-root",
  templateUrl: "landing.html"
})
export class LandingComponent {
  helpState: boolean = false;

  // toggle help on and off
  toggleHelp() {
    if (this.helpState == false) {
      this.helpState = true;
    } else {
      this.helpState = false;
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
