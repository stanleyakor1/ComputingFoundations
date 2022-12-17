from sys import *
from math import *
from convert import *

'''
The code is run on the terminal  with the signs in front of the digits as shown below:

python problem1.py +085205.9563 195046.99855 +384701.2802 183656.33635 

'''

def angle(d1,a1,d2,a2): 
	a=a2-a1;d=d2-d1
	return 2*asin(sqrt((sin(d/2)*sin(d/2))+cos(d1)*cos(d2)*sin(a/2)*sin(a/2)))

def main():
        # converting the input arguements into float, and then computing its value in radians
	y=argv[1];d1=Radian(float(y[0:3]),float(y[3:5]),float(y[5:])).DEC2rad() # angle of declination 
	x=argv[2];a1=Radian(float(x[0:2]),float(x[2:4]),float(x[4:])).RA2rad()  # angle os ascension  
	z=argv[3];d2=Radian(float(z[0:3]),float(z[3:5]),float(z[5:])).DEC2rad() # angle of declination
	w=argv[4];a2=Radian(float(w[0:2]),float(w[2:4]),float(w[4:])).RA2rad()  # angle of ascension
	
	print('{} = {}'.format('The angle between the stars in degrees is', degrees(angle(d1,a1,d2,a2))))
if __name__ == '__main__':
    main()
