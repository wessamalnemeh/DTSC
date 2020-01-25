import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { tileLayer, latLng, Map, LatLng } from 'leaflet';
import 'leaflet';
import 'leaflet.heat'
declare let L;
import { addressPoints } from '../../assets/realworld'

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {


  ngOnInit(): void {
    
  }

  @Input()
  data:any;

  options = {
    layers: [
      L.tileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 12,
        attribution: ""
      })
    ],
    zoom: 8,
    center: L.latLng(52.531677, 13.381777)
  };

  onMapReady(map: Map) {
 
    var addresses=[]
    for(var i=0;i<this.data.length;i++){
      addresses.push( latLng(this.data[i].Lat, this.data[i].Lng))
    }
  
    //addresses.push( latLng(46.879966, -122.726909))
    //addresses.push( latLng(46.879966, -120.726909))
    //let newAddressPoints = addressPoints.map(function (p) { return [p[0], p[1]]; });
    const heat = L.heatLayer(addresses).addTo(map);

  } 



}
