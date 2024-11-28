# Operators are used to perform operation on variables and values

x = 5

# Using plus(+) operator
print(10 + 5) # 15

# Using Floor division
print(20//5)

# Using Exponentiation
print(20**5) # 3200000

# Using Modulus
print(20%5) # 0

# calc_result = x &= 3

x &= 3

y = 7

calc_result2 = x | 3

print('calc_result =>', x, calc_result2)

# Logical Operators
print(y > 3 and x < 10) # True

# Using the or statement to compare between conditions
print(y > 3 or x > 10) # True

# Using the not statement to compare between conditions
print(not(y > 3 or x > 10)) # True

# Identity Operators
print(x is y) # False

print(x is not y) # True

# Membership Operators
fruits = ['apple', 'pineapples']
# Using in operator to check if an item is in a list of sequence
print('banana' in  fruits) # False

# Using not in operator to check if an item is in a list of sequence
print('banana' not in  fruits) # True

# Bitwise Operators
print(x & y)

print(3 << 2)
print(3 >> 2)

# Addition and subtraction has the same precedence and therefore, will be evaluated from left to right
print(5 + 4 - 7 + 3)