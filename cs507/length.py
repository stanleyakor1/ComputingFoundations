from sys import *
f=open(argv[1],'r')
all=f.read()
w=all.split()
count=0
for a in w:
    count=count+1

print('No of word in file =',count)
f.close()
