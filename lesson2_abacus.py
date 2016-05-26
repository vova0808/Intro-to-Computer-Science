#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 




def print_abacus(value):

    #create a dictionary with keys like a numbers in string represantations and
    # their respective values in abacus represantation
    abacuses = {
        "0" : "|00000*****   |",
        "1" : "|00000****   *|",
        "2" : "|00000***   **|",
        "3" : "|00000**   ***|",
        "4" : "|00000*   ****|",
        "5" : "|00000   *****|",
        "6" : "|0000   0*****|",
        "7" : "|000   00*****|",
        "8" : "|00   000*****|",
        "9" : "|0   0000*****|"}

    #create a list for adding a values of abacuses keys that are equal to function input
    lst1 = []

    

    s = str(value) #convert argument to a string
    for i in s:    #iterate over it and over abacuses and check if keys in abacuses are equal to function argument
        for key in abacuses: 
            if i == key: #if it is add respective value from key to lst1
                lst1.append(abacuses[key])

    #check if len lst1 less than 10 add abacuses value of number 0 in the beginning of lst1
    while len(lst1) < 10:
        lst1.insert(0, abacuses["0"])

     
    #iterate over lst1 and for all particular items print it
    for abacus in lst1:
        print abacus
        


                

    
    
    
    
    
            

    

        
    
        
    

    

        
                
    
            

        
