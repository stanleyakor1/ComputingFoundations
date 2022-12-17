from student import *
# user's inputs
a=input("Enter the student's name: ")
b=float(input("Enter the student's grade on midterm exam: "))
c=float(input("Enter the student's grade on final exam: "))
d=input("Enter category (LG or PF): ")
# storing the input information
Name=[a];Midterm=[b];Final=[c];cond=[d]
ask=input('Do you want to continue (Y/N)?: ')
while ask == 'Y':
	a=input("Enter the student's name: ")
	b=float(input("Enter the student's grade on midterm exam: "))
	c=float(input("Enter the student's grade on final exam: "))
	d=input("Enter category (LG or PF): ")
	Name.append(a); Midterm.append(b); Final.append(c); cond.append(d)
	ask=input('Do you want to continue (Y/N)?: ')
# initializing counters for the number of PF and LG students
count1=0;count2=0

Result=[] # bucket for storing the student information (Name and grade)

for i in range(len(cond)):
	if cond[i]=='LG':
		count1+=1
		Info=LGstudent(Name[i],Midterm[i],Final[i])
		Result.append(Info.name+" "+Info.calcGrade())
	else:	
		count2+=1
		Info=PFstudent(Name[i],Midterm[i],Final[i])
		Result.append(Info.name + " "+ Info.calcGrade())

Result=sorted(Result) # sorts the students in alphabetic order

print()
print('NAME','GRADE')
for  i in Result:print(i)
print("Number of letter-grade students: ",count1)
print("Number of pass-fail students: ", count2)


