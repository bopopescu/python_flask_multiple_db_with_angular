var express = require("express");
var cors = require("cors");
var bodyparser = require("body-parser");
var app = express();
var mongoose = require("mongoose");
var MongoClient = require('mongodb').MongoClient;
var a;
app.use(bodyparser.urlencoded({extended:true}))
app.use(bodyparser.json())
app.use(cors())
// var url = "mongodb+srv://smartconnect:smartconnect@cluster0-xivdq.mongodb.net"
var url = "mongodb://127.0.0.1:27017/PFA"
// MongoClient.connect(url,(err,con)=>{
//             if(err)
//             console.log(err)
//             if(con){
//                 // var dbo = db.db("one");
                
//                 console.log("connected")
//             }
//         })

        mongoose.connect(url,{useNewUrlParser:true}).then(() => {
console.log("Connected to Database");
}).catch((err) => {
    console.log("Not Connected to Database ERROR! ", err);
});
// mongoose.connect('mongodb+srv://smartconnect:smartconnect@cluster0-xivdq.mongodb.net/one',{ useNewUrlParser: true },function(err,data){
    // if(err){
        // console.log(err)
    // }/
    // if/(data)
    // {
        // console.log("connected")
    
          
    //     var kannan ={
    //         username:"lachumiraja",
    //         address:"salem",
    //         company:"mnw"
    //      }
    //      kannan.save(function(data,err){
    //          if(err){
    //              console.log(err)
    //          }
    //          if(data)
    //          {
    //              console.log(data,"saved")
    //          }
    //      })
    // }
// })
// var conn = mongoose.Connection;

app.get("/",(req,res)=>{
    res.send("Connected")
    res.end();
})

app.post("/json",(req,res)=>{
console.log(req.body)
 a = req.body;
res.json(req.body);
    res.end();
})

app.get("/getjson",(req,res)=>{
    res.send(a);
})
var port = process.env.PORT || 4000;
app.listen(port)
console.log(port)

