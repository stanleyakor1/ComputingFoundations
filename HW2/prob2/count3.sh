#!/usr/bin/bash
count=0; #Intializing count as zero
for i in *;  # Iterating through each file in the current directory.
	do count=$((count+1)); # updating count for every file
	echo ${i}; # prints the file
 done;
echo "There are $count files in this directory" # the final count is then given as output
