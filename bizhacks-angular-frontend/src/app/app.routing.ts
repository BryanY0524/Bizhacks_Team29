import { AppComponent } from "./app.component";
import { Component } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";

import { ModuleWithProviders } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";

import { ApiService } from "./ApiService";

import { PageDefault } from "./app.pagedefault";
import { PriceMatchComponent } from "./app.pricematch-component";
import { LandingComponent } from "./app.landing";

const appRoutes: Routes = [
  { path: "pricematch", component: PriceMatchComponent },
  { path: "landing", component: LandingComponent },
  { path: "", redirectTo: "/landing", pathMatch: "full" },
  { path: "**", component: PageDefault }
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);
