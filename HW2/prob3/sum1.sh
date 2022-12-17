#!/usr/bin/bash

sum=0; # Initializing the sum as zero
for i  in $@; do # iterating through each input given by the user
	
	sum=$(($sum + $i)); # updating sum with the values of the inputs

	
done

echo $sum # Printing the final sum
