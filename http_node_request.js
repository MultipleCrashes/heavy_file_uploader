var request = require('request');
var sleep = require('sleep');

for (var i =0; i < 500;i++){
	console.log("Request no "+i);
	requestUrl = request('http://localhost:3000',function(error , response, body){
		if(!error && response.statusCode ==200){
			console.log(body);
			}
	})

}
