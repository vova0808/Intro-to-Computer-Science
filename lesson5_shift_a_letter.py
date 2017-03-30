# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

def shift(letter):
    letters = "abcdefghijklmnopqrstuvwxyz"
    target = letters.index(letter)
    if target == len(letters) - 1:
        return letters[0]
    else:
        return letters[target+1]



print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a