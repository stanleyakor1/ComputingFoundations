from sys import *

def leapyear(year):
    isLeapYear = ( year % 4 == 0)
    isLeapYear = isLeapYear and ( year % 100 != 0)
    isLeapYear = isLeapYear or ( year % 400 == 0)
    return(isLeapYear)

def main():
    year = int(argv[1])   
    Y=leapyear(year)
    print(Y)

if __name__ == '__main__':
    main()
