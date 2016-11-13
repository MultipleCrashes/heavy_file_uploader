var mongodb = require('mongodb');
var MongoClient = require('mongodb').MongoClient;
var record1 = {"first_name":"a","last_name":"upadhyay"};
var record2 = {"first_name":"b","last_name":"upadhyay"};
var record3 = {"first_name":"c","last_name":"upadhyay"};
var record4 = {"first_name":"d","last_name":"upadhyay"};
MongoClient.connect("mongodb://localhost:27017/harish",function(err,db){
	   if(!err){
		    console.log("We are connected");
		    db.collection('harish').insert(record1);
	            console.log("Inserging record 1" + record1);     
	            db.collection('harish').insert(record2);
		    console.log("Inseting record 2" + record2);
                    db.collection('harish').insert(record3);
                    console.log("Inserting record 3"+ record3);
		    db.collection('harish').insert(record4);
		    console.log("Inserting record 4"+ record4);
	    } else
	   {
		    console.log("Error in connecting to db" + err);
       }
});
