# Using F-string to aformat strings

text = f"The price is 40 dollars"

# using placeholders

price = 40

txt = f"The price is {price} dollars"

# Using modifiers
text2 = f"The price is {price:.2f} dollars"

print(text2)  # The price is 40.00 dollars

# Perform operations directly
tax = 0.25

text3 = f"the price is {20 * 30} dollars"

text4 = f"the price is {price + (price + tax)} dollars"
print(text4)  # Output: the price is 80.25 dollars


# Execute functions
fruit = "mango"

print(f"{fruit.upper()}")  # Output: MANGO
