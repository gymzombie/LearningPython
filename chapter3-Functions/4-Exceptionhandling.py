def div42by(divideBy):
  return 42 / divideBy
  
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


#------------------ That fails with a Divide-by-zero error
#--- So to do some exception handling, tellit how to handle:

def div42by(divideBy):
  try:
    return 42 / divideBy
  except ZeroDivisionError:
    print('Error: Don't try to divide by zero you dolt.')
  
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
