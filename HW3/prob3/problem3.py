from math import *
from sys import *

r=int(argv[1])
g=int(argv[2])
b=int(argv[3])

if r==0 and g==0 and b==0:
    c=0;m=0;y=0;k=1
else:
    w=max(r/255,g/255,b/255)
    c=(w-(r/255))/w
    m=(w-(g/255))/w
    y=(w-(b/255))/w
    k=1-w
    
print("The conversion in CMYK format is ")
print("  C=",c )
print("  M=",m )
print("  Y=",y )
print("  K=",k )
