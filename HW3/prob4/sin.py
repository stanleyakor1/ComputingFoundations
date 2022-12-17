from math import *
from sys import *
'''The decimal module provides support for fast correctly rounded decimal floating point arithmetic.
reference: https://docs.python.org/3/library/decimal.html'''
from decimal import * # For higher precision, such that the tolerance of 1e-15 can be supported.

x1=float(argv[1]) # Input argument in degrees.

x=Decimal(radians(x1)) # Convert the input degrees  to radians.

SINX=Decimal(sin(x)) 

EPSILON=1e-15 # Tolerance

approx_sin=Decimal(0) # Initialization

n=0

while True:  
    approx_sin+=((-1)**n/Decimal(factorial(2*n+1)))*(x**(2*n+1)) 
    n+=1
    if abs(approx_sin-SINX)<=EPSILON:
        break

print('The approximation of sin',x1,'degrees is',str(approx_sin))
