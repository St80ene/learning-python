# Checking data type of a list
my_list = ['apples', 233, 'banana']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(type(my_list))

# Using the list() constructor to create a list
print(list(('man', 'woman', 1, 3, True, False)))

print(len(my_list))

# Get the last item in a list using negative index
print(my_list[-1]) # banana

print(my_list[-2]) # 233

# Range of indexes
print(my_list[1:2]) # [233]

# Return up to but not including the kiwi
print(thislist[:4]) # ['apple', 'banana', 'cherry', 'orange']

# Leave out the end value, the range will get up to the end of the list
print(thislist[2:]) # ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# Range of negative index for strating from the end of the list
print(thislist[-4:-1]) # ['orange', 'kiwi', 'melon']

# Check if item exists
if 'apple' in my_list:
  print('Yes, Apple is in my list of groceries')
else: 
  print('Apple is not found, try apples')
  
# Change the second item in a list
my_list[1] = 'mango'
print(my_list)

# Change a range of item values
my_list[1:3] = ['blackcurrant', 'Watermelon']

print(my_list)

# Replace an item value with two new values
my_list[0:1] = ['Udara', 'grape']
print(my_list)

# Use insert method to insert a new item into the list using the index
my_list.insert(3, 'cherry')
print(my_list) # ['Udara', 'grape', 'blackcurrant', 'cherry', 'Watermelon']

# Add an item to the end of the list
my_list.append('ncheku')
print(my_list) # ['Udara', 'grape', 'blackcurrant', 'cherry', 'Watermelon', 'ncheku']

# extend a list.
# Add elements of tropical to mylist
tropical = ["mango", "pineapple", "papaya"]
my_list.extend(tropical)

# Add tuple to the list
myTuple = ('standard', 'normal')

my_list.extend(myTuple)

print(my_list) # ['Udara', 'grape', 'blackcurrant', 'cherry', 'Watermelon', 'ncheku', 'mango', 'pineapple', 'papaya', 'standard', 'normal']

# Remove specified item using the remove method
my_list.remove('cherry')
print(my_list) # ['Udara', 'grape', 'blackcurrant', 'Watermelon', 'ncheku', 'mango', 'pineapple', 'papaya', 'standard', 'normal']

# Remove specified index using the pop method(removes last item by defualt if index is not specified)
my_list.pop(2)

print(my_list) # removed 'blackcurrant' ['Udara', 'grape', 'Watermelon', 'ncheku', 'mango', 'pineapple', 'papaya', 'standard', 'normal']

# You can also use the del keyword to remove specified item using index
del my_list[0]

print(my_list) # ['grape', 'Watermelon', 'ncheku', 'mango', 'pineapple', 'papaya', 'standard', 'normal']

# the del keyword can also delete the list completely
# del my_list
print(my_list) # NameError: name 'my_list' is not defined

# Empty the list the clear method
my_list.clear()
print(my_list) # []

# Loop throough a list
for x in tropical:
  print(x)
  
for i in range(len(thislist)):
  print(thislist[i])
  
# using while loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
# Using list comprehension while looping
[print(x) for x in thislist]

# Sort list

this_new_list = [100, 50, 65, 82, 23]

# Sort in ascending order
this_new_list.sort()
print('Sorted in ascending order:', this_new_list)

# Sort in descending order
this_new_list.sort(reverse=True)
print('Sorted in descending order:', this_new_list)

nigerian_languages = ['Ibibio', 'Efik', 'Ikwerre', 'Ogoni', 'Yoruba']
# Case insensitive sorting
nigerian_languages.sort(key = str.lower)

print('Case insensitive sorting',nigerian_languages)

# make a copy of a list 

# Using the Built-in list method
my_nigerian_languages = list(nigerian_languages)

print(my_nigerian_languages)

# using the : operator
new_nigerian_language_list = nigerian_languages[:]

print(new_nigerian_language_list)

# Using the copy method
copied_language_list = nigerian_languages.copy()
print(copied_language_list)

# Join two lists
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list3 = list1 + list2

print('joined list1 and list2 using + method', list3)

for x in list2:
  list1.append(x)
  
print('appended lists', list1)

# using the extend method to join two lists
list1.extend(list2)

print('Joined list by appending', list1)
