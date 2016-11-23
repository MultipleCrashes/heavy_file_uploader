var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');


var url = "mongodb://localhost:27019/harish"

var dbName = "proddb";
MongoClient.connect(url, function(err,db){
   assert(err,null);
   console.log("Sucessfully connected to database");
   //db.collection('proddb', function(err,collection){});
    //collection.insertOne({"a":1});
 });

