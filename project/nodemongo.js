var mongodb = require('mongodb');
var MongoClient = require('mongodb').MongoClient;
var record1 = ({"first_name":"arbind","last_name":"upadhyay"});
var record2 = ({"first_name":"madhu","last_name":"upadhyay"});
var record3 = ({"first_name":"manish","last_name":"upadhyay"});
var record4 = ({"first_name":"asha","last_name":"upadhyay"});
MongoClient.connect("mongodb://localhost:27017/harish",function(err,db){
	   if(!err){
		    console.log("We are connected");
		    db.collection('harish').insertOne(record1);
		    db.collection('harish').insertOne(record2);
		    db.collection('harish').insertOne(record3);
		    db.collection('harish').insertOne(record4);
		  } else
	   {
	           console.log("Error in connecting to db" + err);
	      }
});
