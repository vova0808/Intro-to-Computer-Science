# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    if len(A) == 0 or len(A) != len(A[0]):
        return False
    elif len(A) == 1:
        return True
    else:
        i = 0
        while i <= len(A) - 1:
            j = 0
            while j <= len(A[i]) - 1:
                if not A[i][j] == -A[j][i]:
                    return False
                j+= 1
            i += 1
    return True        
    
