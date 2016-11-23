var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');

var url = "mongodb://localhost:27017/harish";

var dbName = "proddb";

console.log("Connecting to mongodb at ->" + url);

exports.Connect = MongoClient.connect(url, function(err,db){
   if(!err){
   console.log("Sucessfully connected to database");
   var collection = db.collection(dbName);
   console.log(collection.insertOne({"xyz":123}));
   //allDocuments = collection.find({});
//console.log(allDocuments);
   db.close();    // Do not forget to close the db handle 
   }
   else
	{
   	console.log("Could not connect to mongodb database");
	}   
 });





