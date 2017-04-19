# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def convert_list(list_to_convert, previous_list):
    for i in range(1, len(list_to_convert) - 1):
        list_to_convert[i] = previous_list[i] + previous_list[i-1]

    return list_to_convert

def triangle(n):
    result = []
    if n <= 0:
        result.append([])
    elif n == 1:
        result.append([1])
    elif n > 1:
        length = n
        while length >= 1:
            result.insert(0, [1] * length)
            length -= 1
        for j in range(2, len(result)):
            result[j] = convert_list(result[j], result[j - 1])
    return result




#For example:

print triangle(0)
#>>> []

print triangle(1)
#>>> [[1]]

print triangle(2)
#>> [[1], [1, 1]]

print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]




