

if [[ -z $1 ]] 
then
    echo "Give shared folder plz"
    exit
fi
fullfolderName="$PWD/$1"
docker run -it --rm -v $fullfolderName:/GRUV/datasets gruv /bin/bash

