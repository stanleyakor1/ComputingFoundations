from math import *
from sys import *
'''The decimal module provides support for fast correctly rounded decimal floating point arithmetic.
reference: https://docs.python.org/3/library/decimal.html'''
from decimal import * # For higher precision, such that the tolerance of 1e-15 can be supported.
# We evaluate the parameters using the decimal function. 

# User's input
x1=float(argv[1])


'''At x1=0.0, we encounter a singularity. That is, irrespective of the number of interations,
only the first term of the taylor series of cos x1 will be greater than 0. All others will be zero.
'''
if x1==0.0:
    result=1
    print('The approximation of cos',x1,'is',str(result))
else:

    x=Decimal(radians(x1))# Ensures higher precision

    COSX=Decimal(cos(x))

    EPSILON=1e-15 # Tolerance

    approx_cos=Decimal(0)

    m=0
        
    while True:  
        approx_cos+=((-1)**m/Decimal(factorial(2*m)))*(x**(2*m))
        m+=1
        if abs(approx_cos-COSX)<=EPSILON:
            break        
        
    print('The approximation of cos',x1,'degrees is',str(approx_cos))




