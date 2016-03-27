
print('My name is')
for i in range(5):
  print('Jimmy Five Times ' + str(i))
  

# - Equivalent to above  
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1


# Playing with range() options:

for i in range(0, 10, 2):
    print(i)
  
  #----------------------

# This one calculates adding all number from 0-100  
total = 0
for num in range(101):
	total = total + num
print(total)


