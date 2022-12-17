#!/usr/bin/bash

sum=0 # Initializing the value of sum

for ((i=$1;i<=$2;i++)); do # using a c++ style for-loop to iterate through the first and last inputs with a step of 1.

	sum=$(($sum+$i)) # Updating sum
done
echo $sum # printing the final value of sum.
