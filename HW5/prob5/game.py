from problem5 import *
## Driver function 
def Driver(a,b,Mymove,Cmove,Human,Computer):
        # Ensures the user enters the right input
        assert Mymove =='scissors' or Mymove =='rock' or Mymove=='paper',f"{Mymove} is invalid, pick from: scissors,paper,rock "

        print(f"{b} chooses {Cmove}")

        if Mymove == Cmove:
        	print(f"{a}: {Human.getScore()} {b}: {Computer.getScore()}")

        elif (Mymove=='rock' and Cmove == 'scissors') or (Mymove =='scissors' and Cmove=='paper')\
         or (Mymove == 'paper' and Cmove =='rock'):

                Human.Win()
                print(f"{a}: {Human.getScore()} {b}: {Computer.getScore()}")

        else:
            Computer.Win()
            print(f"{a}: {Human.getScore()} {b}: {Computer.getScore()}")
        print()

# request user's inputs
a=input("Enter name of human: ")
b=input("Enter name of computer: ");print()
me=input(f"{a}, enter your choice: ")

Computer=Computer(b);Human=Human(a) # creating objects

Driver(a,b,me,Computer.Cplay(),Human,Computer)
Tries=1
while(Tries<3):

        me=input(f"{a}, enter your choice: ")

        Driver(a,b,me,Computer.Cplay(),Human,Computer)

        Tries+=1

if Computer.getScore()>Human.getScore():print(f'{b.upper()} WINS')
elif Computer.getScore()==Human.getScore():print(f'{a.upper()} and {b.upper()} TIE')
else:print(f'{a.upper()} WINS')











