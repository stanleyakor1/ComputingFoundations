from lgStudent import *

# recieve input from the user
a=input("Enter the student's name: ")
b=float(input("Enter the student's grade on midterm exam: "))
c=float(input("Enter the student's grade on final exam: "))

# Place holder for the inputs received
Name=[a];Midterm=[b];Final=[c]

ask=input('Do you want to continue (Y/N)?: ')

while ask == 'Y':
	a=input("Enter the student's name: ")
	b=float(input("Enter the student's grade on midterm exam: "))
	c=float(input("Enter the student's grade on final exam: "))

	Name.append(a); Midterm.append(b); Final.append(c)

	ask=input('Do you want to continue (Y/N)?: ')

# length of the longest name. This will be helpful in aligning the print outputs.
n=len(max(Name,key=len)) 

# place holder for students grade
Result=[]

for i in range(len(Name)):
        # we create objects from the student class
	Info=LGstudent(Name[i],Midterm[i],Final[i])
        # we compute the student's grade as requried
	Result.append(Info.name+" "*(n-len(Info.name))+" "*3+Info.calcGrade())
Result=sorted(Result) # We sort the students name in alphabetical order

print()
print('NAME'+" "*abs(4-n),'GRADE')
# we print the students information (name and grade)
for i in Result:print(i)

