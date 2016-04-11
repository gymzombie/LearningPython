
# Lists are comma separated

[1, 2, 3]
['cat', 'bat', 'rat', 'elephant']
foo = ['hello', 3.1415, True, None, 42]
print(foo[1])  # returns 3.1415

# lists can be nested

foo = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(foo[1][3])    # returns 2nd list, 4th entry. In this case, that's 40. 

# Negative numbers start counting from the end, with -1 
foo = [10, 20, 30, 40, 50]
print(foo[-1])    # Returns 50
print(foo[-2])    # returns 40

# Can be returned as strings
foo = ['cat', 'bat', 'rat', 'elephant']
print('The ' + foo[0] + ' is afraid of the ' + foo[-2] +'.')


# A "Slice" is like a range of a list
foo[1:3]      # Returns ['bat', 'rat']
              # Catch here is that it goes up to, //but doesn't include// the third one. 

# Can assign a new value to an index:
foo = ['cat', 'bat', 'rat', 'elephant']
foo[1] = 'gorilla'
foo     # Returns ['cat', 'gorilla', 'rat', 'elephant']

  # Also, can ADD to the list, as well as replace with a slice. For example:
foo[3:5] = ['monkey', 'lion', 'giraffe']
foo    # Returns ['cat', 'gorilla', 'rat', 'monkey', 'lion', 'giraffe']   

# Delete with "del" command. It acts like an "unassignment"
del foo[1]    # returns ['cat', 'rat', 'monkey', 'lion', 'giraffe']

len(foo)     # counts the items. In this case, returns 5


list('Hello')
=> ['H', 'e', 'l', 'l', 'o']

# Can test to see if something is included
'monkey' in foo    # returns True




              



