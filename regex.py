import re

# using the re module for RegEx

text = "The rain in Spain"

pattern_match = re.search("^The.*Spain$", text)

if pattern_match:
    print("pattern matched")
else:
    print("no match")

find_all_matches = re.findall("ai", text)

print(find_all_matches)  # Output: ['ai', 'ai']

try:
    print(find_all_matches)
except:
    print("Exception occured")
else:
    print("Else part")


try:
    print("Testing the try part")
except:
    print("it's not working")
finally:
    print("All operations done")
