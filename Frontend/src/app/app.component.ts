import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import {DTSCService} from './dtsc.service';



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
  diseases = [
    {value: 'niereninsuffizienz', viewValue: 'Niereninsuffizienz'},
  ];

  cities = [
    {value: 'berlin', viewValue: 'Berlin'},
  ];



  constructor(private DTSCService: DTSCService,private route: ActivatedRoute,public router: Router){
    
  }

  ngOnInit(): void {
    this.submitQuery();
  }

  submitQuery(){
    this.render=false
    this.DTSCService.clusterQuery("niereninsuffizienz","berlin")
    .subscribe(dataSource => {
      this.clusters=dataSource
      this.clusterElements=this.clusters[0].elements
      this.render=true
    });
  }

  displayCluster(clusterNumber){
    console.log(clusterNumber)
    this.clusterElements=this.clusters[clusterNumber-1].elements
  }
 
}
