# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.



def numbers_in_lists(string):
    #inserted list
    lst = []

    
    result = []

    #add first element from string to result
    result.append(int(string[0]))

    for elem in string[1:]:
        #check if element in string starting from second element is greater then last element in result
        if int(elem) > result[-1]:
            #if yes add this elem to result and clear lst
            result.append(int(elem))
            lst = []

        #if last element in result is list    
        elif type(result[-1]) == list:
            #check previous element in result, if it less than element from string, then add element from string to result
            if result[-2] < int(elem):
                result.append(int(elem))
                #clear lst
                lst = []
            else:
                #else, add element from string to inserted list in result
                result[-1].append(int(elem))
        else:
            #if last element from result less than elem from string, then add element from string to  list lst and add lst to result
            lst.append(int(elem))
            result.append(lst)
    return result        
