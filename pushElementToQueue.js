var redis = require('redis');


var redisConnect = function(){

        var client = redis.createClient(6379,'127.0.0.1');
	
	client.on('connection',function(){
		console.log('redis connected');
	});

		client.set('taskharish','taskid123');
		client.set('task2','harish2');
		client.quit();
}

var pushToQueue = function(elementToPush){
	var queue = [];
	queue.push(elementToPush);
	console.log("Elements in the queue are "+ elementToPush);
     }

redisConnect();
pushToQueue("harish");
pushToQueue(123);
module.exports.pushToQueue = pushToQueue;
module.exports.redisConnect = redisConnect;
