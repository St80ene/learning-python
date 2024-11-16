b = 'Hello World'

# Slicing a string, using start and end points
print(b[1:10])

# Slicing a string, without specifying start point
print(b[:10])

# Slicing a string, without specifying end point
print(b[2:])

# Using negative indexing to start slicing from the end of a string
# Get the character "o" to but not included: "d" in "World"
print(b[-5:-2])

# Remove whitespaces
c = "characters   "
print(c.strip())

# Convert string to uppercase
print(c.upper())

# Convert string to lowercase
print(c.lower())

# Replace string with another
print(c.replace('c', 'R'))


# Split string using delimiter
string_example = 'Hi there'
print(string_example.split(' '))

# Concatenate strings
string_example1 = 'Hi there'
string_example2 = 'Etiene'
print(string_example1 + " " + string_example2)

# Format strings
age = 56
print(f'I am {age + 5} years old')

# Format with decimal
price = 1208
print(f'fuel is {price:.2f} Naira')

# add math operation and format
txt1 = f"The price is {20 * 59} dollars"
print(txt1)

# Escape characters
print("We are the \"creators\" of the world.")
