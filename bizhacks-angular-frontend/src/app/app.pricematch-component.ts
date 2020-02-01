import { Component } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { ApiService } from "./ApiService";

@Component({
  selector: "app-root",
  templateUrl: "pricematch.html"
})
export class PriceMatchComponent {
  productPrice = "";
  productName = "";
  productImageUrl = "";

  _apiService: ApiService;
  public site = "http://localhost:5000/";

  // API SERVICE
  constructor(private http: HttpClient) {
    // Pass in http module and pointer to AppComponent.
    this._apiService = new ApiService(http, this);
    this.getProductData();
  }

  // GETTING PRODUCT DATA
  getProductData() {
    this._apiService.getData("", this.productDataCallback);
  }
  productDataCallback(result, _this) {
    if (result.errorMessage == "") {
      _this.productImageUrl = result.img_url;
      _this.productName = result.name;
      _this.productPrice = result.price;
      console.log(result);
    } else {
      alert("Unable to get data");
    }
  }
}