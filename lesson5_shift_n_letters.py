# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
# negative or zero.

def shift_n_letters(letter, n):
    letters = "abcdefghijklmnopqrstuvwxyz"
    target = letters.index(letter)
    if n > 0:
        if target + n > len(letters) - 1:
            return letters[(target + n) - len(letters)]
        else:
            return letters[target + n]
    elif n < 0:
        return letters[n + target]
    else:
        return letters[target]


print shift_n_letters('s', 1)
# >>> t
print shift_n_letters('s', 2)
# >>> u
print shift_n_letters('s', 10)
# >>> c
print shift_n_letters('s', -10)
# >>> i