#!/usr/bin/bash
count=0; # Initializing the count as zero
for f in *.txt;   # Interating through each file with a .txt extension
	do count=$((count+1)); # Count is updated for every .txt file
 done;
echo $count


