print(10 > 9)

a = 15
b = 20

if b > a:
  print('b is greater than a') # True
else: 
  print('a is greater than b')
  

print(9 > 18) # False

# Evaluate a string using bool() method in python
print(bool('Hello')) # True
print(bool(15)) # True
print(bool('')) # False. Empty strings are always False
print(bool([])) # False.Empty list are always False
print(bool(())) # False. Empty tuple are always false
print(bool({})) # False. Empty dict are always False

# Any object created from a class with the __len__ function returns 0 or False
class Car():
  def __len__(self):
    return 0
  
myCar = Car()

print(bool(myCar)) # False

# Functions can return boolean

def myFunc():
  return True

print(myFunc()) # True


def myFunc2():
  return False

print(myFunc2()) # False

# Check if an object is an integer or not
x = 300
print(isinstance(x, int)) # True