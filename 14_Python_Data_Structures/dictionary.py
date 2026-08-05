data = {"name" : "Sam", "age" : 20}
print(data)

# Creating a dictionary
a = {"x": 1, "y": 2}
print(a)

b = dict(name="Sam", age=20)
print(b)

# Accessing a dictionary
d = {"name": "Kat", "age": 21}

print(d["name"])     # Access using key
print(d.get("age"))  # Access using get()

# Adding and updating dictionary items
d = {"name": "Sam"}

d["age"] = 21        # Adding a new key-value pair
d["name"] = "Alex"   # Updating an existing value
print(d)

# Reomving dictionary items
d = {"a": 1, "b": 2}
del d["a"]
print(d)

# Iterating through a dictionary
d = {"a": 1, "b": 2}
for key in d:
    print(key)
    
d = {"a": 1, "b": 2}
for value in d.values():
    print(value)
    
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)