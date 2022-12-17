#!/usr/bin/bash

rand=$(($RANDOM %51)) # Generates a random number between 0 and 50.
U_l=50 # upper limit
L_l=0 # Lower limit
Tries=0 # Initializing the number of tries as zero

while [ "$guess" != "$rand" ]  #Checks if the guess is not equal to the generated random number
do

 if [ "$Tries" -eq 0 ]; then       # At the first instance where number of tries is zero, echo the following

echo "The magic number is between 0 and 50"
echo -n "Make your guess:  "; read guess

else

    if [[ $guess -lt $rand && $(($U_l-$guess)) -gt 1 ]]; then
        L_l=$(($guess+1))  #    Updating the lower limit
    
    elif [[ $guess -lt $rand && $(($U_l-$guess)) -eq 1 ]]; then # Ensures that the difference between the upper and lower limit is greater than or equal to one. 
      L_l=$guess
    
    elif [[ $guess -gt $rand && $(($guess-$L_l)) -gt 1 ]]; then
     
          U_l=$(($guess-1))  # Updating the upper limit

    elif [[ $guess -gt $rand && $(($guess-$L_l)) -eq 1 ]]; then    # Ensures that the difference between the upper and lower limit is greater than or equal to one
      U_l=$guess
    fi

echo "The magic number is between $L_l and $U_l" # Gives the user an information about a smaller range where the answer lies.
echo -n  "Make your guess: "; read guess

fi


Tries=$(($Tries+1)) # Updating tries

  if [ $guess -lt $rand ]; then # Checks if the guess is less than the answer

        echo " $guess is too low "

  elif [ $guess -gt $rand ]; then # Checks if the guess is greater than the answer

        echo " $guess is too high" 

  else
        echo " You got it in $Tries guesses"
    exit
  fi
  
done
