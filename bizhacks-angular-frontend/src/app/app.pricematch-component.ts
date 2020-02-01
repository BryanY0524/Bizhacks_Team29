import { Component } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { ApiService } from "./ApiService";
import { NgxSpinnerService } from "ngx-spinner";


@Component({
  selector: "app-root",
  templateUrl: "pricematch.html"
})
export class PriceMatchComponent {
  productPrice = "";
  productName = "";
  productModel = "";
  productImageUrl = "";
  spinnerStatus: boolean = false;
  stores = [["Amazon"], ["Walmart"]]
  priceMatchToggle: boolean = false;

  _apiService: ApiService;
  public site = "http://localhost:5000/";

  // API SERVICE
  constructor(private http: HttpClient, private spinner: NgxSpinnerService) {
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
      _this.productModel = result.model_num;
      _this.productPrice = result.price;
      console.log(result);
    } else {
      alert("Unable to get data");
    }
  }

  getPrices() {
    this.priceMatchToggle = true;
    this.spinnerStatus = true;

    this._apiService.getData("product" + "/" + this.productName + "/" + this.productModel, this.getPricesCallback)
  }

  getPricesCallback(result, _this) {
    console.log(result);  
    
    // turn off spiner
    if (result.Amazon == "Undefined") {
      _this.stores[0][1] = "Not Available"
    } else {
      _this.stores[0][1] = result.Amazon;
    }
    if (result.Walmart == "Undefined") {
      _this.stores[1][1] = "Not Available"
    } else {
      _this.stores[1][1] = result.Walmart;
    }

    console.log(_this.store);
    _this.spinnerStatus = false;
  }


}
