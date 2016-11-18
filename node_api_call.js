var http = require('http');
var fs = require('fs');

function send404(response){
     response.writeHead(404, {"Content-Type":"text/plain"});
     response.write("Error 404 : Page not found");
     response.end();

}

// handle user request 
function onRequest(request,response){
    if( request.method == 'GET' && request.url == '/' )
    {
	    response.writeHead(200,{"Content-Type":"text/html"});
	    fs.createReadStream("./index.html").pipe(response);
    }
    else{
	    send404(response);
    }


}


http.createServer(onRequest).listen(8080);
console.log('Server is now running at 8080 port...');



