from sys import *

def binary(value): 
    if value==0: return None # if value is zero, the function returns nothing.
    binary(value//2) # recursive step for the continual division by 2.
    print(value%2,end='') # Prints the remainder
def main():
    value=int(argv[1])
    binary(value);print()
if __name__ == '__main__':
    main()

