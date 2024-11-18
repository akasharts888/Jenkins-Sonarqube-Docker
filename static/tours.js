// import {TabulatorFull as Tabulator} from 'tabulator-tables';
//define some sample data
var tabledata = [
    {id:1, name:"The Sea Explorer", duration:4, location:"Miami, USA"},
    {id:2, name:"The Forest Hiker", duration:6, location:"Banff, CAN"},
    {id:3, name:"The Snow Adventurer", duration:4, location:"Forests"},
    {id:4, name:"The Forest Hiker", duration:4, location:"Forests"},
    {id:5, name:"The Forest Hiker", duration:4, location:"Forests"},
];

//create Tabulator on DOM element with id "example-table"
var table = new Tabulator("#table_body", {
    height:205, // set height of table (in CSS or here), this enables the Virtual DOM and improves render speed dramatically (can be any valid css height value)
    data:tabledata, //assign data to table
    layout:"fitColumns", //fit columns to width of table (optional)
    columns:[ //Define Table Columns
        {title:"ID", field:"id"},
        {title:"Name", field:"name"},
        {title:"Duration (in days)", field:"duration", hozAlign:"center"},
        {title:"Location", field:"location"},
    ],
});

