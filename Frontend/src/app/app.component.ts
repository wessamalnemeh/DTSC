import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import {DTSCService} from './dtsc.service';
import { MapComponent } from './Map/map.component';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
 
  title = 'Frontend';
  clusterElements:any=[]
  clusters:any=[]
  render=false;
  loader=false
  selectedCity="berlin"
  selectedDisease="husten"
  selectedAnimal="not-specified"

  @ViewChild('map',{static: false})
  private mapComponent: MapComponent;

  
  diseases = [
    {value: 'husten', viewValue: 'Husten'},
    {value: 'schnupfen', viewValue: 'Schnupfen'},
    {value: 'pruritus', viewValue: 'Pruritus'},
    {value: 'leishmaniose', viewValue: 'Leishmaniose'},
    {value: 'niereninsuffizienz', viewValue: 'Niereninsuffizienz'},
  ];

  cities = [
    {value: 'berlin', viewValue: 'Berlin'},
  ];


  animals = [
    {value: 'not-specified', viewValue: 'Not specified'},
    {value: 'Katze', viewValue: 'Cat'},
    {value: 'Hund', viewValue: 'Dog'},
  ];



  constructor(private DTSCService: DTSCService,private route: ActivatedRoute,public router: Router){
    
  }

  ngOnInit(): void {
    
  }
  search(){
    this.render=false
    this.loader=true
    this.submitQuery(this.selectedDisease,this.selectedCity,this.selectedAnimal);
  }

  submitQuery(disease,area,animal){
    this.render=false
    this.DTSCService.clusterQuery(disease,area,animal)
    .subscribe(dataSource => {
    
      if(dataSource.Error==undefined){
      this.clusters=dataSource
      this.clusterElements=this.clusters[0].elements
      this.render=true}else{
        alert("No result !!")
        this.render=false
        this.loader=false
      }

    });
  }

  displayCluster(clusterNumber){
    console.log(clusterNumber)
    this.clusterElements=this.clusters[clusterNumber-1].elements
    this.mapComponent.refreshMap(this.clusterElements);
  }
 
}
