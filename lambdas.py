from functools import reduce

# Lambdas are functions that has no name(anonymous)

x = lambda a : a + 10
print(x(5))

# Accept many arguments
multiply_nums = lambda a, b : a * b

print(multiply_nums(2, 3)) # Outpit: 6

add_nums = lambda a, b, c, d, e : a + b + c + d + e

print(add_nums(2, 3, 6, 7, 9)) # Outpit: 6

def reduce_num():
  numbers = [1, 2, 3, 4, 5, 6]
  result =  reduce(lambda x, y : x * y, numbers)
  
  return result

print(reduce_num())

def squared_nums():
  numbers = [1, 2, 3, 4, 5, 6]
  return list(map(lambda x : x * x, numbers))

print(squared_nums()) # Output: [1, 4, 9, 16, 25, 36]

fruits = ['Strawberry', 'Pawpaw', 'Orange', 'Banana']

sorted_list = sorted(fruits, key = lambda x: len(x))

print(sorted_list) # Output: ['Pawpaw', 'Orange', 'Banana', 'Strawberry']

pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
  
    