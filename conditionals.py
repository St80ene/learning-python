a = 5
b = 10

# if...else
if a > b:
  print('a is greater than b')
else:
  print('a is less than b')
  
# elif
if b > a:
  print('b is greater than a')
elif a == b:
  print('b is not greater than a')
  
# combine if with elif and else to catch exceptions
if b < a:
  print('b is less than a')
elif b > a:
  print('b is greater than a')
else:
  print('they are equal')
  
# shorthand if
if a > b: print('a is greater than b')

# shorthand if else
print('b is less than a') if b > a else print('b is greater than a')

# one line if else statement with 3 conditions
print('A') if a > b else print('b') if b > a else print('they are the same')

# using 'and' to combine logical statements
x = 200
g = 33
h = 500
if h > x and h < b:
  print('they are both true')
else:
  print('Both conditions are not true')
  
# using the 'or' keyword to reverse the result of the conditional statements
if h > a or h < a:
  print('One of the conditions is true')
  
# using the 'not' keyword to reverse the result of the conditional statements

if not a > b:
  print('A is less than b')
  
# Nested if statements
if a > b:
  print('above 5')
  
  if b > a: 
    print('less than 5')
  else:
    print('equal to 5')
    
# using the 'pass' keyword to bypass empty if statement
if a > b:
  pass