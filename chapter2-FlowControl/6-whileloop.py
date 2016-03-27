spam = 0
while spam <5:
  print('Hello World!')
  spam = spam + 1
  
#--------------------

name = ''                           # Programmer humor
while name != 'your name':          
    print('Please type your name.')
    name = input()                  
print('Thank you!')                 

#---------------------

while True:                         # This is the same as above, but uses a break instead
    print('Please type your name.')
    name = input()                  
    if name == 'your name':         
        break                       
print('Thank you!')                 
