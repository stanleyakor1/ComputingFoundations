from sys import *
import dateofweek
from leapyear import *

def calendar(m,year):
    # Preparing strings and list for the weeks, months and days in a calendar

    week=['Su','Mo','Tu','We','Th','Fr','Sa']
    months=['January','February','March','April','May','June','July','August','September','October','November','December']
    ndays=[31,28,31,30,31,30,31,31,30,31,30,31]


    # We want to know what day is the first of the month being considered
    start=int(dateofweek.day(m,1,year)) 

    if leapyear(year): # If the year being considered is a leap year, February becomes 29 days
        ndays[1]=29
         
    print('{0} {1}'.format(months[m-1], year).center(20, ' '))
    print(''.join(['{0:<3}'.format(j) for j in week]))
    print('{0:<3}'.format('')*start, end='')

    for day in range(1, ndays[m-1] + 1):
        print('{0:<3}'.format(day), end='')
        start += 1
        if start == 7:   # Once start is equal to 7, print on the next line        
            print()
            start = 0 
    print('\n')

def main():
    m=int(argv[1]) # month in consideration
    year=int(argv[2]) # year being considered
    calendar(m,year)
if __name__ == '__main__':
    main()
