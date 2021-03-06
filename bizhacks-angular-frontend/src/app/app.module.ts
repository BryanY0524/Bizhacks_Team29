import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { TooltipModule } from "ngx-bootstrap/tooltip";
import { ModalModule } from "ngx-bootstrap/modal";

import { AppComponent } from "./app.component";
import { HttpClientModule } from "@angular/common/http";

import { NgxSpinnerModule } from "ngx-spinner";

import { FormsModule } from "@angular/forms";
import { routing } from "./app.routing";

import { PageDefault } from "./app.pagedefault";
import { PriceMatchComponent } from "./app.pricematch-component";
import { LandingComponent } from "./app.landing";
import { TVQuestionComponent } from "./app.tvquestion";
import { ProductsComponent } from "./app.products"

@NgModule({
  declarations: [
    AppComponent,
    PageDefault,
    PriceMatchComponent,
    LandingComponent,
    TVQuestionComponent,
    ProductsComponent
  ],
  imports: [
    BrowserModule,
    TooltipModule.forRoot(),
    ModalModule.forRoot(),
    HttpClientModule,
    FormsModule,
    routing,
    NgxSpinnerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
