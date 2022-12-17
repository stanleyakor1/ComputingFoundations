from sys import *

class LGstudent:
    # constructor that takes in the student's attributes e.g name
    def __init__(self,name: str,midterm:float,final: float):
        self.name=name
        self.midterm=midterm
        self.final=final
        # avoiding negative values inputs
        assert midterm>=0,f"Midterm score {self.midterm} must be greater than or equal to zero"
        assert final>=0,f"Final score {self.final} must be greater than or equal to zero"
    def setName(self,other):
        self.name = other    
    def setMidterm(self,other):
        self.midterm = other
    def setFinal(self,other):
        self.final = other
    # function that calculates the student's grade
    def calcGrade(self):
        grade=(self.midterm+self.final)/2.0
        if grade >=90.0: return 'A'
        if 90.0>grade>=80.0: return 'B'
        if 80.0>grade>=70.0: return 'C'
        if 70.0>grade>=60.0: return 'D'
        return 'F'
    # string function
    def __str__(self):
        return f"{self.name}'s grade based on {self.midterm} and {self.final}"  
# a test function    
def main():
    Info=LGstudent(argv[1],float(argv[2]),float(argv[3]))
    print(f"{Info} is {Info.calcGrade()}")

if __name__=='__main__':
    main()
