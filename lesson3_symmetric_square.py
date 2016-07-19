# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(lst):
    if len(lst) == 0:
        return True
    elif len(lst) != len(lst[0]):
        return False
    elif len(lst) == 1:
        for i in lst:
            if len(i) == 1:
                return True
    
    else:
        i = 0
        while i <= len(lst) - 1:
            j = 0
            while j <= len(lst[0]) - 1:
                if lst[i][j] != lst[j][i]:
                    return False
                j += 1
            i += 1
    return True        
