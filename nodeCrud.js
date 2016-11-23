var MongoClient = require('mongodb').MongoClient;


exports.insertOne(db,collection,document,callback){

	var collection = db.collection(collection);
	collection.insertOne(document);
});
