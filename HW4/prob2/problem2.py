def Multiply(A,B):
    #checking if the number of rows and columns of both matrices are same.
    assert (len(A)==len(A[0])) and (len(B)==len(B[0])), " Both matrices must be square and with the same dimension "
    nr=len(A); # returns the number of rows in matrix A"
    M=[([0]*nr) for i in range(nr)] # Initializing the matrix that stores the result of the multiplication"
    for i in range(nr): 
        for j in range(nr):
            for k in range(nr):
                M[i][j]+=A[i][k]*B[k][j] # rewriting the mathematical expression for matrix multiplication
    return M

# Code implementation    

def main():
    A=[[1,2,3],[4,5,6],[7,8,9]]
    B=[[9,8,7],[6,5,4],[3,2,1]]
    M=Multiply(A,B)
    for i in M: print(i)
if __name__ == '__main__':
    main()


