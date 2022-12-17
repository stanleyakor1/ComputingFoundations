from sys import *

def day(m,d,y):
    y0=y-(14-m)//12
    x=y0+y0//4-y0//100+y0//400
    m0=m+12*((14-m)//12)-2
    return (d+x+(31*m0)//12)%7

def main():
    m = int(argv[1])
    d = int(argv[2])
    y = int(argv[3])
    D=day(m,d,y)
    print(D)

if __name__ == '__main__':
    main()
