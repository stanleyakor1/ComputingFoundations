from sys import *


# system arguments
x=float(argv[1]); y=float(argv[2]); z=float(argv[3])


# conditionals
if (x>y and y>z) or (x<y and y<z):
    print(True)
else:
    print(False)
    
