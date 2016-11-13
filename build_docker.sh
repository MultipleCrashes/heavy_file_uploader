backend_branch="PRE_PROD"

echo "Taking pull of -> "$backend_branch
git pull origin $backend_branch
backend_image_name="backend_pre_prod" 
subsequent_container="$(docker images $backend_image_name | tail -n+2 | head -1 | awk '{ print $1 ":" $2+0.01 }')"
echo "Building subsequent container -> ${subsequent_container}"
docker build -t ${subsequent_container} . 
docker run -dp 8010:8000 --env-file env.list ${subsequent_container}
echo docker run -dp 8002:8000 --env-file env.list ${subsequent_container}

