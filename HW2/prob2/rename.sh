#!/usr/bin/bash

for i in *.txt; do # Iterating through each .txt file in the directory  
    
    mv $i $(date +%Y-%m-%d)-"$i" # using the move command in conjunction with the date command to change the file name

 done;


