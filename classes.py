# Using the class keyword to create a class.A class is a blueprint for creating an object

class Person:
  name = 'Etiene'
  
person = Person()

print(person.name)


# using the __init__() to assign values. It is being called automatically, anytime the function is being used to create objects
class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
person2 = Person2('Chidera', 45)

print(person2.name)
print(person2.age)


# Using the __str__() to represent the class as a string
class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  # Note: the self parameter is a reference to the instance of a class
  def __str__(self):
    return f"{self.name}({self.age})"
    
person3 = Person3('David', 56)
print(person3)


# Classes can also have methods, just like objects. 
# Add a function to the class to print a greeting

class Greeting:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def send_greeting(self):
    return f"Hello, {self.name}"
  
greet_user = Greeting('Paschal', 78)
print(greet_user.send_greeting())

# Modify object property
greet_user.name = 'Ifeanyi'

print(greet_user.name)

# Delete object property
del greet_user.age

# Using the pass statement to avoid getting error if the class has no content
class Fruit:
  pass