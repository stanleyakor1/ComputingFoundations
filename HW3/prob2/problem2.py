from math import *
from sys import *

'''
Since the task requires us to  compute the great-circle distance between Paris and San Francisco
we pre-condition our code such that if the user does not insert the coordinates on the command line
for the prefered locations. The program automatically computes the great-circle distance between
Paris and San Francisco.
'''

if len(argv) == 1: # Case where the user does not supply a command line arguement.
    x1=radians(48.87)  # Converts degrees to radian
    y1=radians(-2.33)
    x2=radians(37.8)
    y2=radians(122.4)
                    
else: # Case where the user supplies command line arguements
    x1=radians(float(argv[1])) # Converts degrees to radian
    y1=radians(float(argv[2]))
    x2=radians(float(argv[3]))
    y2=radians(float(argv[4]))

# Distance
d=60*degrees(acos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2)))

print('The distance between the places in nautical miles is:',d)

