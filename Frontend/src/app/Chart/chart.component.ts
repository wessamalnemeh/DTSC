import { Component, OnInit, Input ,Output, EventEmitter} from '@angular/core';
import * as Highcharts from 'highcharts';
import highcharts3D from 'highcharts/highcharts-3d.src';
highcharts3D(Highcharts);

@Component({
  selector: 'app-chart',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.css']
})
export class ChartComponent implements OnInit {


    @Input()
    data:any;

    @Output() 
    valueChange = new EventEmitter();

   /* title = 'Date X PLZ';
    type='ScatterChart';
    chartData = [];
    columnNames = ['Date'];
    options = {   
    };
    width = 600;
    height = 500;

    ngOnInit(): void {
        for(var i=0;i<this.data.length;i++){
            var clusterName:string='Cluster'+(i+1)
            this.columnNames.push(clusterName)
            for(var j=0;j<this.data[i].elements.length;j++){
                let arr = new Array<number>(this.data.length+1);
                arr[0]=this.data[i].elements[j].Date
                arr[i+1]=this.data[i].elements[j].Region
                this.chartData.push(arr)
            }
        }
    }

    onSelect(event){
        if(event!=undefined && event.length>0){
            if(event[0].row==null)
                 this.valueChange.emit(event[0].column);
        }
    }*/

   highcharts = Highcharts;
   chartOptions = {      
    chart: {         
       type: 'scatter',
       marginBottom: 100,
       marginRight: 50,
       options3d: {
          enabled: true,
          alpha: 10,
          beta: 30,
          depth: 250,
          viewDistance: 5,
          frame:{
             bottom :{
                size: 1,
                color: 'rgba(0, 0, 0, 0.02)'
             },
             back :{
                size: 1,
                color: 'rgba(0, 0, 0, 0.04)'
             },
             side :{
                size: 1,
                color: 'rgba(0, 0, 0, 0.06)'
             }
          }
       }
    },         
    title : {
       text: '3D Scatter Plot'   
    },
    plotOptions: {
        series: {
            turboThreshold:3000,
            cursor: 'pointer',
            point: {
                events: {
                    click: function(e){
                       const p = e.point
                       this.onSelect(p.category,p.series.name);
                    }.bind(this)
                }
            }
        }
    },
    series : []
 };

   ngOnInit(): void {


    for(var i=0;i<this.data.length;i++){
        //var clusterName:string='Cluster'+(i+1)
        //this.columnNames.push(clusterName)
        var clusterName:string='Cluster'+(i+1)
        var serie={name:clusterName,data:[]}
        for(var j=0;j<this.data[i].elements.length;j++){
            let arr = new Array<number>(3);
            arr[0]=this.data[i].elements[j].Lat
            arr[1]=this.data[i].elements[j].Lng
            arr[2]=this.data[i].elements[j].Date
            serie.data.push(arr)
        }
        this.chartOptions.series.push(serie)
    }

    console.log(this.chartOptions.series)
 

   }
   onSelect(category,name){
    this.valueChange.emit(parseInt(name[7]));
 
   }

}
