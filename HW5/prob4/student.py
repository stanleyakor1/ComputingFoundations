class Student():

    def __init__(self,name: str,midterm:float,final: float):
        self.name=name
        self.midterm=midterm
        self.final=final
        # Ensuring that the input is non-negative
        assert midterm>=0,f"midterm exams score {midterm} is invalid"
        assert final>=0,f"final exams score {final} is invalid"
    def setName(self,other):
        self.name = other

    def setMidterm(self,other):
        self.midterm = other

    def setFinal(self,other):
        self.final = other

    def calcGrade(self):
        grade=(self.midterm+self.final)/2.0
        if grade >=90.0: return 'A'
        if 90.0>grade>=80.0: return 'B'
        if 80.0>grade>=70.0: return 'C'
        if 70.0>grade>=60.0: return 'D'
        return 'F'
    def __str__(self):
        return f"{self.name}'s grade based on {self.midterm} and {self.final} is"  
        
class LGstudent(Student): # we aren't adding any new features
    pass

class PFstudent(Student):
    def __init__(self,name: str,midterm:float,final: float):

        super().__init__(name,midterm,final)
    # redefining the calcGrade function for the subclass
    def calcGrade(self):
        grade=(self.midterm+self.final)/2.0

        if grade >=60: return 'Pass'
        return 'Fail'




