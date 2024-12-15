import datetime

from datetime import datetime

def greeting(name):
  current_datetime = datetime.now()
  
  current_hour = current_datetime.now().hour
  
  add_name_greeting = ''
  
  if 4 <= current_hour <= 12:
     add_name_greeting = f"Good morning {name}"
  elif 12 >= current_hour <= 17 :
    add_name_greeting = f"Good afternoon {name}"
  else:
     add_name_greeting = f"Good evening {name}"
    
  print(add_name_greeting)
  


greeting('Etiene')


# How to practice function using an app(greeting app) using python or any other ideas

# How to create a function in python
def first_function():
  print('This is my first function in python')
  
first_function()

# If number of args not known, you can use an asterisk '*'
def my_kids(*kids):
  print(f"one of my kids is {kids[1]}")
  
my_kids('Etiene', 'Funmi', 'Deborah')

# You can also use double asterisks ** in front of the parameter to represent unknown number of args
def my_kids_2(**kids):
  print(f'His last name is {kids['lname']}')
  
# You can also use the key = value pair to provide args
my_kids_2(fname = 'Tobias', lname = 'Etiene')

# Default params value
def my_country(country = 'Nigeria'):
  print(f'{country} is my Homeland!!!')
  
my_country() # prints Nigeria is my Homeland!!

# Passing a list as an argument
def my_fruit_bowl(fruits):
  fruit_string = ", ".join(fruits)
  print(f"My fruit bowl consists of {fruit_string}")

my_fruit_bowl(['Strawberry', 'guava', 'mango', 'orange', 'banana'])

# Positional arguments in Python: any parameters passed to that function must follow the order in which they were assigned as arguments. Order matters and no explicit keywords allowed.

def test_pos_arg(name, age):
  print(f"{name} is {age} years old")
  
test_pos_arg('Elaise', 20) # Output: Elaise is 20 years old

# Keyword arguments mean you can supply the arguments to a function by calling the keywords and assigning the value using an equal sign. order doesn't matter and you use explicit keywords to pass arguments.
def test_keywrd_args(name, age):
  print(f"{name} is {age} years old")
  
test_keywrd_args(age = 30, name = 'Elijah') # Output: Elijah is 20 years old

# You can combine both styles but positional arg(s) must come before keyword arg(s)

def greet_customer(name, age, greeting):
  print(f"{greeting}, {name}, You are {age} years old" )
  
greet_customer('Isaac', age = 20, greeting = 'Hi' )

# You can specify that a function can only have positional args by adding ",/" after the parameters

def test_only_pos_args(name, age, /):
  print(f"Your name is {name}, You are {age} years old.") 
  
# test_only_pos_args(name = 'Raeghar', age = 45) 
''' Error output:     test_only_pos_args(name = 'Raeghar', age = 45)
TypeError: test_only_pos_args() got some positional-only arguments passed as keyword arguments: 'name, age 
'''

test_only_pos_args('Raeghar',45) # Works for only positional args

# You can specify that you want only keywords args by adding "*, " before the parameters
def test_only_keywrd_args(*, name, age,):
  print(f"Your name is {name}, You are {age} years old.") 
  
# test_only_keywrd_args('Elaise', 35)
'''
Error output test_only_keywrd_args('Elaise', 35)
TypeError: test_only_keywrd_args() takes 0 positional arguments but 2 were given
'''
test_only_keywrd_args(name = 'Elaise', age = 35)

# You can combine two args types in a function. positional must come before keywords. any argument before ,/ a re positional, any args after * are keywords only
def print_greeting(fname, age, /, *,  title, lname):
  print(f"{title} {fname} {lname} is {age} years old.")
  
print_greeting('Damola', 20, title = 'CEO', lname = 'Adeniyi' )

# Functions can also be recursive in Python
def tri_recursion(k):
  if (k > 0):
    recursion_res = tri_recursion(k - 1)
    print('recursion_res: ', recursion_res)
    result = k + recursion_res
    print(result)
  else :
    result = 0
  return result
  
tri_recursion(6)