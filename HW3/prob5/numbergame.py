from random import *

RAND=randrange(0,51) # Generates a random number between 0 and 50

U_L=50; # Upper limit of the random range
L_L=0; # Lower limit of the random range
Tries=0; # number of attempts

while True:
    if Tries==0:
        print('The magic number is between', L_L,' and ', U_L)
        guess=int(input('Make your guess: '))
        
    
    else:
        
        if (guess<RAND) and ((U_L-guess)>1): # Updating the lower limit
            L_L=guess+1
        elif (guess<RAND) and ((U_L-guess)==1): # Ensures that the difference between the upper and lower limit is greater than or equal to one
            L_L=guess
        elif (guess>RAND) and ((guess-L_L)>1): # Updating the upper limit
            U_L=guess -1
        else: # Ensures that the difference between the upper and lower limit is greater than or equal to one                    
            U_L=guess
            
            
        print('The magic number is between', L_L,' and ', U_L) # Gives the user an information about a smaller range where the answer lies.
        guess=int(input('Make your guess: '))
        
        
    Tries+=1 # Updating tries
    if guess<RAND:# Checks if the guess is less than the answer
        print(guess,'is too low ')
    elif guess>RAND: # Checks if the guess is greater than the answer
        print(guess,'is too high ')
    else:
        print('You got it in',Tries,'guesses')
        break   
