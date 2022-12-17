#!/usr/bin/bash
a=$1 # The first input of the user
sum=0 # Initializing the value of sum as zero

while [ "$a" -le $2 ]  # Iterating through the first and second inputs of the user.
do
	sum=$(($sum+$a)) # upating sum 
	a=$(($a+1)) # updating the firt input
done
echo $sum # printing the final value of sum
