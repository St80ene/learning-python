# Variables created outside a function


x = "great" # global variables

'''
def myFirstFunct():
  print('Python is ' + x)
  
myFirstFunct()
'''


'''
def printName():
  x = 'Etiene' # variable in a function
  print('name', x)
  
printName()
'''


'''
def printName():
  global name  # Using the global keyword to define a variable. It makes the scope to be global.
  name = 'Etiene' # variable in a function
  print('name', name)
  
printName()
'''

name = "Essenoh"

def printName():
  global name  # Using the global keyword to reassign a value.
  name = 'Etiene' # variable in a function
  print('name', name)
  
printName()