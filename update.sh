#!/bin/bash

#read -p "Would you like to update? (y/N) " answer
#if [ "$answer" == "n" ] || [ "$answer" == "N" ] || [ "$answer" == "" ]
#then
	#echo "Update aborted"
	#exit
#fi

# Update System
#echo -e "\eStep 1. Updating system\e"
#sudo apt update
#sudo apt upgrade -y

# Install dependencies
# git, vim

# Create symbolic link to service file

# Update Campervan version
echo -e "\eStep 2. Updating campervan version\e"
git pull origin master
softwareVersion=$(git describe --long)

# Restart campervan service
sudo service campervan restart
