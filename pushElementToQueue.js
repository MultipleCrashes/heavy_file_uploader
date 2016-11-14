

var pushToQueue = function(elementToPush){
	var queue = [];
	queue.push(elementToPush);
	console.log("Elements in the queue are "+ elementToPush);
     }

pushToQueue("harish");
pushToQueue(123);
module.exports.pushToQueue = pushToQueue;
