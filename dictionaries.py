# Dictionaries are ordered and changeable and can contain any data type
my_details = {
  "first_name": "Etiene",
  "last_name": "Etiene",
  "complexion": "dark-skinned",
  "years_of_experience": 4,
  "colors": ['white', 'black']
}

# can be referenced using key
print(my_details["complexion"]) # dark-skinned

# using len to know how many items are in  dictionary
print(len(my_details)) # 4

# using type to determine type of a dictionary
print(type(my_details)) # <class 'dict'>

# using dict() constructor to create a dictionary
new_dict = dict(name = 'John', age = 56, colors = ['blue', 'purple'])
print(new_dict) # {'name': 'John', 'age': 56, 'colors': ['blue', 'purple']}

# using the get method to access dictionary items
first_name = my_details.get('first_name')
print(first_name) # Etiene

# using keys method to return all the keys in a dictionary
my_detail_keys = my_details.keys()
print(my_detail_keys) # dict_keys(['first_name', 'last_name', 'complexion', 'years_of_experience', 'colors'])

my_car = {
  'brand': 'Lexus',
  'model': 2025
}

# add item to the list and print the keys
my_car['color'] = 'white'
print(my_car) # {'brand': 'Lexus', 'model': 2025, 'color': 'white'}

# using values method to get the values in a dict
my_car_values = my_car.values()
print(my_car_values) # dict_values(['Lexus', 2025, 'white'])

# change the value of an item and print
my_car['color'] = 'black'

print(my_car) # {'brand': 'Lexus', 'model': 2025, 'color': 'black'}

# using the items method to return each item as a tuple
dict_items = my_car.items()
print(dict_items) # dict_items([('brand', 'Lexus'), ('model', 2025), ('color', 'black')])

# check if key exists
if 'color' in my_car:
  print('Yes, car has color') # Yes, car has color
else:
  print('No, car has no color')
  
# using the update method to update a dict
my_car.update({'tyres': 4})

print(my_car) # {'brand': 'Lexus', 'model': 2025, 'color': 'black', 'tyres': 4}

# using the pop() nmethod to remove item with the key name
my_car.pop('color')
print(my_car) # {'brand': 'Lexus', 'model': 2025, 'tyres': 4}

# using popitem() method to remove the last inserted item
my_car.popitem()
print(my_car) # {'brand': 'Lexus', 'model': 2025}

# using the del keyword to remove an item with the specified key
del my_car['brand']
print(my_car) # {'model': 2025}

# using the clear() method to clear the dict
my_car.clear()
print(my_car) # {}

# using a for loop to iterate over a dict
for x in my_details:
  print(x)
  
# inserting the items one at a time
for x in my_details:
  print(my_details[x])
  
# using the values() method to print all the values
for x in my_details.values():
  print(x)

# using the keys() method to print all the keys
for x in my_details.keys():
  print(x)
  
# loop through both keys and values by using items() method
for x,y in my_details.items():
  print(x, y)
  
# using the built-in copy method to copy a dict
new_details = my_details.copy()
print(new_details) # {'first_name': 'Etiene', 'last_name': 'Etiene', 'complexion': 'dark-skinned', 'years_of_experience': 4, 'colors': ['white', 'black']}

# or by using the dict() method
new_details2 = dict(my_details)
print(new_details2) # {'first_name': 'Etiene', 'last_name': 'Etiene', 'complexion': 'dark-skinned', 'years_of_experience': 4, 'colors': ['white', 'black']}

# a dict can contain nested dict

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# access items in nested dicts
print(myfamily['child1']['name']) # Emil

# loop through nested dict uding items() method
for x, obj in myfamily.items():
  
  for y in obj:
    print(y + ':', obj[y])