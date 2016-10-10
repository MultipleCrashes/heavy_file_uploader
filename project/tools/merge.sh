ter_branch="PRE_PROD"


echo "The script for merging branch will execute, it takes branch to be merged."
echo "Last commit id "
echo "-----------------------"
git log --format="%H" -n 1
echo "-----------------------"
echo "git checkout ${master_branch}"
git checkout $master_branch
echo "git pull origin ${master_branch}"
git pull origin $master_branch
echo "git fetch && git checkout ${1}" 
git fetch && git checkout $1
echo "git pull origin ${1}"
git pull origin $1
echo "git merge ${master_branch}"
git merge $master_branch 
echo "git checkout ${master_branch}"
git checkout $master_branch
echo "git merge ${1}"
git merge $1
read -p "Are you sure , you want to push the changes to remote ?" -n 1 -r 
if [[ $REPLY =~ ^[Yy]$ ]] 
        echo
then
                echo "git push origin  ${master_branch}"
                        git push origin $master_branch
                fi


