# Guess the number game - Not currently working.


import random

print('Hello. What is your name?')
name = input()
print('Well, ' + name + ', I am thinking of a number between one and 20.')
secretNumber = random.randint(1, 20)


def validGuess():
  print('Take a guess.')
  try:
    guess = int(input())
  except ValueError:
    print('You have to input a number')
    continue
  if 1 <= guess <= 20:
    return guess
  else:
    print('Pick a number between 1 and 20')     

for guessesTaken in range(1, 7):
  validGuess()
  if guess < secretNumber:
    print('Your guess is too low.')
  elif guess > secretNumber:
    print('Your guess is too high.')
  else:
    break # This is for the correct guess
    
if guess == secretNumber:
  print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
  print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
