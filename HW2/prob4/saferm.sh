#!/usr/bin/bash


arg=$1 # First input by the user

if [ $# -gt 1 ]; then # checks if the number of input is greater than 1

	echo You have given too many inputs 
	exit # terminate the program if input argument is greater than 1
else
	if [ ! -d removed_files/ ]; then # Checks if the directory doesnt exist
  		mkdir  removed_files/; # if true, it creates the directory
  	else
  		echo  directory already exist, process continuing! # The directory exists

  		#continue # continue subsequent operations
	fi

	cp $arg removed_files/ # copy the file to the folder

	rm $arg # delete the original file
fi
