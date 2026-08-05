# Creating a list
a = [1, 2, 3]
print(a)

b = ["apple", "banana"]
print(b)

# Accesing elements of list
a = [10, 20, 30]
print(a[0])
print(a[-1])

# Adding elements
a = [1, 2]
a.append(3)
print(a)

# Updating element
a = [10, 20, 30, 40, 50]
a[1] = 25
print(a)

# Removing element
a = [1, 2, 3]
a.remove(2)
print(a)

# Iterating over list
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)