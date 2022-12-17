import math
import sys

def evaluate(x,a):
    S=0
    for i in range(len(a)-1,-1,-1):
        S=a[i]+(x*S)
    return S

def exp(x,n):
    # n refers to the n terms of the Taylor series expansion
    a=[1.0/float(math.factorial(i)) for i in range(0,n)] # coefficients of the taylor series
    return evaluate(x,a)

def main():
    x = int(sys.argv[1])
    n = int(sys.argv[2])
    Result=exp(x,n)
    diff=math.exp(x)-Result
    print(Result)
    print('The difference is: ',diff)
    
if __name__ == '__main__':
    main()
