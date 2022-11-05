#A square matrix MM is said to be:
#diagonal: if the entries outside the main-diagonal are all zeros
#scalar: if it is a diagonal matrix, all of whose diagonal elements are equal
#identity: if it is a scalar matrix, all of whose diagonal elements are equal to 11
#Write a function named matrix_type that accepts a matrix MM as argument and 
# returns the type of matrix. It should be one of these strings: diagonal, scalar, identity, non-diagonal. 
# The type you output should be the most appropriate one for the given matrix.
#You do not have to accept input from the user or print output to the console. You just have to write the function definition.

def matrix_type(M):
    l = len(M)
    diag = True
    for i in range(l):
        for j in range(l):
            if i!=j and M[i][j]!=0:
                diag = False
                break
            
    if diag == True:
        scal = True
    else:
        scal = False
    if scal == True:
        x = M[0][0]
        for i in range(l):
            for j in range(l):
                if i==j and M[i][j]==x:
                    scal = True
    
    if scal == True:
        id = True
    else:
        id = False
    if id == True:
        for i in range(l):
            for j in range(l):
                if i==j and M[i][j]==1:
                    id = True
        
    
    
    if scal == True:
        return("Scalar")
    elif diag == True:
        return("Diagonal")
    elif id == True:
        return("Identity")
    else:
        return("Non-Diagonal")