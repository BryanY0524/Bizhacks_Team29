import { Component } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { ApiService } from "./ApiService";

@Component({
    selector: "products",
    templateUrl: "products.html"
})
export class ProductsComponent {
    public localsite = "http://localhost:4200/";
    counter = 0;

    timer = setInterval(this.next, 1000)

    next() {
        this.counter += 1;
        if (this.counter == 8) {
            window.location.href = this.localsite + "pricematch"
        }
    }

    back() {
        if (this.counter < 2) {
            console.log("beginning of qs")
        } else
            this.counter -= 1
    }
}
