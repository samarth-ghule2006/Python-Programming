# Creating a set
s = {1, 2, 3, 4}
print(s)

# Unordered, Unindexed and Mutability
s = {3, 1, 4, 1, 5, 9, 2}

print(s) 
try:
    print(s[0])
except TypeError as e:
    print(e)
    
# Adding element
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
print(s)

# Accessing element
s = {"Geeks", "For", "Geeks"}

for i in s:
    print(i, end=" ")

print("\n", "Geeks" in s)

# Removing element
s = {1, 2, 3, 4, 5}
s.remove(3)
print(s)  