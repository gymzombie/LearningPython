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

# A break ceases the execution and leaves the loop without rechecking the condition

while True:                         # This is the same as above, but uses a break instead
    print('Please type your name.')
    name = input()                  
    if name == 'your name':         
        break                       
print('Thank you!')                 


#------------------------
#   Continue Statements:
# Continue "goes back to the beginning of the of the loop and re-check the condition

while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':       #(1)
    continue              #(2)
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)

# ------------------------
