import { Component } from '@angular/core';
import { tileLayer, latLng, Map, LatLng } from 'leaflet';
import 'leaflet';
import 'leaflet.heat'
declare let L;
import { addressPoints } from '../assets/realworld'



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Frontend';
  options = {
    layers: [
      L.tileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 18,
        attribution: ""
      })
    ],
    zoom: 5,
    center: L.latLng(-37.87, 175.475)
  };

  onMapReady(map: Map) {
    // Do stuff with map
    var addresses=[]
    addresses.push( latLng(46.879966, -121.726909))
    addresses.push( latLng(46.879966, -122.726909))
    addresses.push( latLng(46.879966, -120.726909))
    let newAddressPoints = addressPoints.map(function (p) { return [p[0], p[1]]; });
    const heat = L.heatLayer(newAddressPoints).addTo(map);

  } 
 
}
