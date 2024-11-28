fruit_tuple = ('apple', 'banana', 'watermelon')

# data type of tuple
print(type(fruit_tuple))

# Creating tuple with only one member: add comma else python won't recognize it as a tuple
single_member_tuple = ('apples',)

# Using the tuple constructor to create a tuple
this_tuple = tuple(('apples', 'cherry', 'lemon', 'kiwi', 'avocado', 'star-fruit'))

print(this_tuple)

# Access tuple item using index in square bracket
print(this_tuple[1])

# using negative index to start from the end
print(this_tuple[-1])

# getting a range of items
print(this_tuple[2:4])

# How to update or change a tuple: convert into a list,change and convert back to tuple
car_brands = ('Toyota', 'Hyundai', 'Lexus')

# Convert to a list
converted_tuple = list(car_brands)
# Update one of the items
converted_tuple[1] = 'Lamborghini'

# add a new item
converted_tuple.append('Ferrari')

# Convert back to tuple and print
converted_back_tuple = tuple(converted_tuple)

print('converted_back_tuple', converted_back_tuple) # ('Toyota', 'Lamborghini', 'Lexus', 'Ferrari')

programming_language = ('Python', 'Javascript', 'Perl', 'Pascal', 'Cobol')
# unpacking a tuple
(lang1, lang2, lang3, lang4, lang5) = programming_language

print(lang1, lang2, lang3, lang4, lang5)

# Using Asterisk to assign variables as list to a variable name
(lang16, lang12, *lang) = programming_language
print(lang16, lang12, *lang)

(lang126, *lang123, lang_last) = programming_language
print(lang126)
print(*lang123)
print(lang_last)

# Using for loop to iterate over a tuple
for x in programming_language:
  print('looping through a tuple using for loop', x)
  
# Looping through the index numbers
for i in range(len(programming_language)):
  print('inside for loop =>',programming_language[i])
  
# using while loop to iterate over a tuple
index = 0
while index < len(programming_language):
  print('inside while loop =>', programming_language[index])
  index += 1
  
# Join two tuples using + operator
program_cars = programming_language + car_brands

print('program_cars', program_cars) # ('Python', 'Javascript', 'Perl', 'Pascal', 'Cobol', 'Toyota', 'Hyundai', 'Lexus')


# Multiply tuples
multiple_cars = car_brands * 2
print('multiple_cars', multiple_cars) # ('Toyota', 'Hyundai', 'Lexus', 'Toyota', 'Hyundai', 'Lexus')


# Tuple Methods

# Count
javascript_programming_lang_count = programming_language.count('Javascript')

print('javascript_programming_lang_count', javascript_programming_lang_count) # 1

# search using the index method
python_programming_lang_index = programming_language.count('Python')

print('python_programming_lang_index', python_programming_lang_index) # 1
