// import {TabulatorFull as Tabulator} from 'tabulator-tables';
//define some sample data
var tabledata = [
    {id:1, role:"admin", name:"Krish", phone: 8888888888, email:"krish@example.com" , address:"New Delhi"},
    {id:2, role:"admin", name:"Akash", phone: 8888888888, email:"akash@example.com" , address:"New Delhi"},
    {id:3, role:"admin", name:"Ayush", phone: 8888888888, email:"ayush@example.com" , address:"New Delhi"},
    {id:4, role:"admin", name:"Dalima", phone: 8888888888, email:"dalima@example.com" , address:"New Delhi"},
    {id:5, role:"admin", name:"Sunny", phone: 8888888888, email:"sunny@example.com" , address:"New Delhi"},

];

//create Tabulator on DOM element with id "example-table"
var table = new Tabulator("#table_body", {
    height:205, // set height of table (in CSS or here), this enables the Virtual DOM and improves render speed dramatically (can be any valid css height value)
    data:tabledata, //assign data to table
    layout:"fitColumns", //fit columns to width of table (optional)
    columns:[ //Define Table Columns
        {title:"ID", field:"id", width:70},
        {title:"Role", field:"role", width:100},
        {title:"Name", field:"name", width:100},
        {title:"Phone no.", field:"phone", width:100},
        {title:"Email", field:"email", hozAlign:"center", width:250},
        {title:"Address", field:"address", hozAlign:"center", width:100}
       ],
});
