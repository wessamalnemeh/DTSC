import { Component, OnInit, Input ,Output, EventEmitter} from '@angular/core';


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

    title = 'Date X PLZ';
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
    }

}
