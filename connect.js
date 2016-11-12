var connect = require('connect');
var http = require('http');

var app = connect();

function doFirst(request,response,next){
	console.log("hey there entry part of app");
	next();
}

function doSecond(request,response,next){
	console.log("2nd function call");
	next();
}


app.use(doFirst);
app.use(doSecond);

http.createServer(app).listen(8080);
console.log('Server is running at port 8080..');

