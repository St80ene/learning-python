# Create a set: Sets are unordered, unindexed, no duplicate members and unchangeable
new_set = {'first', 'second', 'third', 'fourth'}
print(new_set)

# True and 1 are considered the same values in set and are treated as one
new_set2 = {False, 0, 'four', 'three', 'two', 'one'}
print('new_set2', new_set2)

# length of a set
print(len(new_set2))

# data type of a set
print('data type of a set', type(new_set2)) # <class 'set'>

# using the set() constructor to make a set
this_set = set(('hint', 'fine', 'boy', 'flex'))

print('this_set', this_set) #  {'boy', 'hint', 'fine', 'flex'}

# Set can consist of different data types bbubt cn't contain lists and dictionaries
varied_set = {'string', True, 87, ('apple',)}
print(varied_set)

# acessing items in a set can be done using for loop or in keyword
for x in varied_set:
  print(x)
  
# Check if people is present in varied_set
print('people' in varied_set) # False

# Check if people is not present in varied_set
print('people' not in varied_set) # True

# Change a set by adding using the add method
varied_set.add('test')
print('add to a set => ', varied_set)


new_varied_set = {'fist', 'legs', 100, ('new tuple', 'inside new tuple')}

new_list = ['kiwi', 'mango', 'blueberries']

# add elements of a list to a set
new_varied_set.update(new_list)
print(new_varied_set) # {'legs', 100, 'mango', 'blueberries', 'kiwi', ('new tuple', 'inside new tuple'), 'fist'}

# Add two sets by using the update method
varied_set.update(new_varied_set)
print(varied_set) # {True, 'legs', 100, 'mango', ('apple',), 'blueberries', 'string', 'kiwi', ('new tuple', 'inside new tuple'), 'test', 87, 'fist'}

# using the remove method to remove an item from a set
varied_set.remove('fist') # throws error if it does not exist
print(varied_set)

# Removeing an item by using the discard method
varied_set.discard('string')
print(varied_set)

# remove a random item by using pop method
varied_set.pop()
print(varied_set)

# using the clear method to empty a set
new_varied_set.clear()
print(new_varied_set) # set()

# using del keyword to delete a set completely
# del new_varied_set
# print(new_varied_set) # NameError: name 'new_varied_set' is not defined. Did you mean: 'varied_set'?

# Joining two sets

# using union to join two set
first_set = {'a', 'b', 'c', 'd', 'e'}
second_set = {'f', 'g', 'h', 'i', 'j', 'k', 'l'}

joined_first_sec_sets = first_set.union(second_set)

print('joined_first_sec_sets', joined_first_sec_sets) # {'a', 'b', 'd', 'e', 'g', 'f', 'k', 'h', 'l', 'j', 'i', 'c'}

# using | instead of union method

joined_first_sec_sets2 = first_set | second_set
print('joined_first_sec_sets2', joined_first_sec_sets2) # {'a', 'b', 'd', 'e', 'g', 'f', 'k', 'h', 'l', 'j', 'i', 'c'}

# join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

# Note: you can only use | to join set with set and not with other data types
merged_sets = set1.union(set2, set3, set4)
merged_sets2 = set1 | set2 | set3 | set4 # using the |
print('merged_sets', merged_sets) # {1, 2, 3, 'a', 'b', 'c', 'bananas', 'John', 'apple', 'Elena', 'cherry'}
print('merged_sets2', merged_sets2) # {1, 2, 3, 'a', 'b', 'c', 'bananas', 'John', 'apple', 'Elena', 'cherry'}

# join a set and tuple
new_tuple2 = ('tuple item1', 'tuple item 2')
joined_tuple_set = set1.union(new_tuple2)

print(joined_tuple_set) # {'b', 'tuple item1', 'tuple item 2', 'c', 'a'}

# Using the update method to join sets
set1.update(set2) # does not return new array and no duplicate item
print(set1) 

# Both union and update methods will exclude duplicate items

# using intersection to return only the duplicates
set12 = {'apple', 'laptop', 'male', 'life'}
set21 = {'male', 'person', 'life'}
set32 = set12.intersection(set21) # returns new array
print('set32 =>', set32) # {'life', 'male'}

# Using the & method instead of intersection to get same result
set33 = set12 & set21 # this method can only be sued to join set to set and not other data types
print('set33', set33) # {'life', 'male'}

# keep only duplicates by using the intersection_update method
set102 = {"apple", "banana", "cherry"}
set201 = {"google", "microsoft", "apple"}
set102.intersection_update(set201)
print(set12) # {'apple'}

# joining sets that contain False, True, 0, 1
set45 = { 1, 0, 'ship', 'sail'}
set46 = {False, True}
set47 = set46.intersection(set45)
print('set47 =>', set47) # {False, True}

# using the difference method to return a new set that contain items not present in the second but are in the first set
differemce_set1 = {'apple', 'google', 'microsoft'}
differemce_set2 = {'apple', 'nvidia', 'facebbook'}
new_difference_set = differemce_set1.difference(differemce_set2)
print(new_difference_set) # {'google', 'microsoft'}

# using the - sign instead of difference
new_difference_set2 = differemce_set1 - differemce_set2

print(new_difference_set2) # {'google', 'microsoft'}

# Using difference_update() to return items present in the first set but not in the second set
differemce_set1.difference_update(differemce_set2)
print(differemce_set2) # {'apple', 'nvidia', 'facebbook'}

# using symmetric_difference method to keep items not present in both sets
symmetric_diff_set1 = {'google', 'apple', 'microsoft'}
symmetric_diff_set2 = {'google', 'apple', 'microsoft','nvidia'}
symmetric_diff_set3 = symmetric_diff_set1.symmetric_difference(symmetric_diff_set2)
print('symmetric_diff_set3 =>', symmetric_diff_set3) # {'nvidia'}

# using the ^ operator instead
symmetric_diff_set4 = symmetric_diff_set1 ^ symmetric_diff_set2

print(symmetric_diff_set4) # {'nvidia'}

# using symmetric_update to keep those that don't have duplicates
symmetric_diff_set1.symmetric_difference_update(symmetric_diff_set2)
print(symmetric_diff_set1) # {'nvidia'}


