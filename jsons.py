import json

# Using json module to parse and stringify objects

x = '{"name": "Etiene", "age": 30}'

stringified_obj = json.loads(x)

print(stringified_obj)  # Output:  {'name': 'Etiene', 'age': 30}

# Converts to json
print(json.dumps(stringified_obj))  # Output:  {"name": "Etiene", "age": 30}

print(
    json.dumps(
        {"name": "Ifeanyi", "color": "black"},
        indent=4,
        separators=(" ", " "),
        sort_keys=True,
    )
)
print(json.dumps(["coconut", "guava", "mango"]))
print(json.dumps("hello"))
print(json.dumps(102))
print(json.dumps(False))
print(json.dumps(True))
print(json.dumps(None))
