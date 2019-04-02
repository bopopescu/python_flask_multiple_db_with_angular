var jwt  = require("jsonwebtoken");
var express = require("express");
var bodyParser = require("body-parser");
var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}))
// app.use(bodyParser.json()); // only parses json data
// app.use(bodyParser.urlencoded({ // handles the urlencoded bodies
//     extended: true
// }));

var token = jwt.sign({ name:"hello" }, "happyworld", {
  expiresIn:30
});
var sec = 1;
var clear = setInterval(()=>{
  console.log(sec++)
  jwt.verify(token,"happyworld",function(err,data){
    if(err){
      console.log(err)
      console.log(err.name)
      console.log(err.message)
      console.log(err.expiredAt)
      clearInterval(clear)
      // process.exit();
    }
    if(data){
      console.log(data)
    }
  })
},1000)

app.post('/token',function (req,res){
  
  jwt.verify(req.headers.token,req.body.pwd,function(err,data){
    if(err)
    {
      res.send({"name":err.name,"message":err.message,"expiredAt":err.expiredAt})
      res.end();
    }
    if(data){
      res.send("Hai your are valid !")
      res.end();
    }
  })
  // console.log("mytoken header",req.headers.token)
  // console.log(req.body)
  // res.end();
})

  console.log(token)
app.listen(3000)