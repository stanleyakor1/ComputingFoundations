R=1.097*1e-2 # Rydberg constant
n1=0;n2=0;n3=0; 
for i in range(1,4):  #  range of m values i.e m=1,2,3.
    if i==1:  # Lyman series
# Since m=1, we begin our range from 2 because we'll have
#zero divion, for any range  of integer value equal to m'''
        for j in range(2,7): # range of five values
                if n1==0:
                    print('Series for m = 1')
                    n1+=1
                # Computing and printing the wavelength    
                print(' ',1/(R*(1/i**2 -1/j**2)),'nm') 
                
# Since m=2, we begin our range from 3, because at m=2 we'll have
#zero divion. For any range of integer value less than m, we'll get 
#negative wavelength which is scientifically wrong.

    elif i==2: # Balmer series
        for j in range(3,8):  # range of five values
                if n2==0:
                    print('Series for m = 2')
                    n2+=1
                # Computing and printing the wavelength       
                print(' ',1/(R*(1/i**2 -1/j**2)),'nm')
                
    else: # Paschen series
        for j in range(4,9): 
                    if n3==0:
                        print('Series for m = 3')
                        n3+=1
                    # Computing and printing the wavelength   
                    print(' ',1/(R*(1/i**2 -1/j**2)),'nm')


