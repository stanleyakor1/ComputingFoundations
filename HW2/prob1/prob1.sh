#!/usr/bin/bash

File="/home/STANLEYAKOR/CS507/HW1/readme.txt" # File location

if [[ -e $File ]]; then   # Checks if the file exists
	echo " The file exits "

        # Since the file exists, we want to check if it is writable

	if [[  -w $File ]]; then # Checks if the file is writable

		echo " File is writable"
	else
		echo " File is not writable" 
	fi
else
	# If file doesnt exits, no need to check if it is writable or not
	echo "The file does not exist, thus not writable"

fi
	
