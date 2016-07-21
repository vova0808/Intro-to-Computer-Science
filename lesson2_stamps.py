# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.



def stamps(pence):
    
    remainder = 0
    fives = 0
    twos = 0
    ones = 0
    
    if pence == 0:
        result = (0,0,0)
    else:
        if pence >= 5:
            fives = int(pence / 5)
            remainder = pence % 5
            if remainder % 2 != 0:
                twos = int(remainder/2)
                ones = 1
            else:
                twos = int(remainder /2)
                ones = 0
        elif pence >= 2:
            fives = 0
            twos = pence % 2
            if twos != 0:
                ones = 1
            else:
                ones  = 0
        elif pence == 1:
            fives = 0
            twos = 0
            ones = 1
            
    return fives, twos, ones            
                
                
            
                 

            
       
        
