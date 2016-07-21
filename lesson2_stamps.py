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
                
                
            
                 

            
       
        
