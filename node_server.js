var http = require('http');

function onRequest(request,response){
	   console.log("A user made a request"+request.url); 
	      response.writeHead(200,{"Context-Type":"text/plain"});
	         response.write("Hey there harish is your response");
		    response.end();
}

http.createServer(onRequest).listen(8080);
console.log('Server is now running at 8080 port...');




