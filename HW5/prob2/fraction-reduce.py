from fraction import *
# user's input
a=int(input('Enter numerator of the fraction: '))
b=int(input('Enter denominator of the fraction: '))

assert b!=0,f"denominator {b} should not be zero"

gcd=Fraction.GCD(Fraction,a,b)
print(f'Reduction to lowest terms: {int(a/gcd)}/{int(b/gcd)}')
