// import {TabulatorFull as Tabulator} from 'tabulator-tables';
//define some sample data
// fetch('/').then(respose=>respose.json()).then(data=>console.log(data.columns)).catch(error=>console.error('Error:',error))
var tabledata = [
    
    {id:1, user_id:"1234", date:"01-12-2023", time:"1:00", guests:5 , tour:"The Forest Hiker", start_date:"10-12-2023", end_date:"14-12-2023"},
    {id:2, user_id:"1234", date:"01-12-2023", time:"1:00", guests:5 , tour:"The Forest Hiker", start_date:"10-12-2023", end_date:"14-12-2023"},
    {id:3, user_id:"1234", date:"01-12-2023", time:"1:00", guests:5 , tour:"The Forest Hiker", start_date:"10-12-2023", end_date:"14-12-2023"},
    {id:4, user_id:"1234", date:"01-12-2023", time:"1:00", guests:5 , tour:"The Forest Hiker", start_date:"10-12-2023", end_date:"14-12-2023"},
    {id:5, user_id:"1234", date:"01-12-2023", time:"1:00", guests:5 , tour:"Hello World", start_date:"10-12-2023", end_date:"14-12-2023"},
];

//create Tabulator on DOM element with id "example-table"
var table = new Tabulator("#table_body", {
    height:205, // set height of table (in CSS or here), this enables the Virtual DOM and improves render speed dramatically (can be any valid css height value)
    data:tabledata, //assign data to table
    layout:"fitColumns", //fit columns to width of table (optional)
    columns:[ //Define Table Columns
        {title:"ID", field:"id", width:70},
        {title:"User ID", field:"user_id", width:100},
        {title:"Date", field:"date", hozAlign:"center", width:100},
        {title:"Time", field:"time", width:80},
        {title:"Guests", field:"guests", hozAlign:"center", width:80},
        {title:"Tour Booked", field:"tour", hozAlign:"center", width:250},
        {title:"Start Date", field:"start_date", hozAlign:"center", width:100},
        {title:"End Date", field:"end_date", hozAlign:"center", width:100},
    ],
});


