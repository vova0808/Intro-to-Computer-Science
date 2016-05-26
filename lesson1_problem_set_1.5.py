# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

# ENTER CODE BELOW HERE
first = text.find('zip')
second = text[first+1:].find('zip')
if second > 0:
    result = (first + second) + 1
else:
    result = -1
    
print result





# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function
