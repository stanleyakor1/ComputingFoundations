from fraction import *
a=input('Enter a posittive decimal number less than 1: ')

# convert the input to its equivalent fraction form so we can apply the gcd.
n=len(a); NUMERATOR=int(float(a)*10**(n-1));
DENOMINATOR=10**(n-1)

gcd=Fraction.GCD(Fraction,NUMERATOR,DENOMINATOR)
print(f'Converted to fraction: {int(NUMERATOR/gcd)}/{int(DENOMINATOR/gcd)}')
