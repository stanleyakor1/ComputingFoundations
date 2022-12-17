#!/usr/bin/bash


bash sum4.sh  # runs the sum4.sh  

if [ "$?" -eq 0 ]; then # checks if exit status is zero
 echo "Command succeeded"
else # otherwise
 echo "Attn: Command failed"
fi





