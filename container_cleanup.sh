echo "Make sure exited containers are deleted"
echo 
sleep 1
docker rm $(sudo docker ps -q -f status=exited)
echo "Make sure unwanted dangling images are removed"
echo 
sleep 1 
docker rmi -f $(sudo docker images -q -f dangling=true)
echo "Clean up and reclaim volume "
docker volume rm $(sudo docker volume ls -qf dangling=true) 
echo "Remove old unused docker containers"
sleep 1 
docker rm $(docker ps -a | grep -v latest | grep -v CONTAINER | awk '{print $1}')
echo "Remove old unused docker images"
sleep 1 
docker rmi $(docker images -a | grep '<none>' | awk '{print $3}')

