import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { LeafletModule } from '@asymmetrik/ngx-leaflet';
import { MapComponent } from './Map/map.component';
import { HttpClientModule } from '@angular/common/http';
import { GoogleChartsModule } from 'angular-google-charts';
import { ChartComponent } from './Chart/chart.component';
import { FlexLayoutModule } from '@angular/flex-layout';

import { MatInputModule,MatSelectModule,MatOptionModule, MatButtonModule} from "@angular/material";
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
//import { HighchartsChartModule } from 'highcharts-angular';

import { HighchartsChartComponent } from 'highcharts-angular';

@NgModule({
  declarations: [
    AppComponent,
    MapComponent,
    ChartComponent,
    HighchartsChartComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    LeafletModule.forRoot(),
    HttpClientModule,
    GoogleChartsModule,
    FlexLayoutModule,
    MatInputModule,
    MatSelectModule,
    MatOptionModule,
    MatButtonModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
