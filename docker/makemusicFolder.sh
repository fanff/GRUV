#!/bin/bash

if [[ -z $1 ]] 
then
    echo "Give shared folder plz"
    exit
fi

mkdir -p $1
mkdir -p "$1/YourMusicLibrary"
mkdir -p "$1/YourMusicLibrary/wave"
mkdir -p "$1/YourMusicLibrary/tmp"

cp sampleConfig.json $1/config.json

echo "Done folder $1"
