# Creating a string
a = 'GFG'  
b = "GeeksForGeeks"  
print(a)
print(b)

# Multi-Line string
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

# Accessing string
s = "ABCDEF"
print(s[0])   
print(s[4])

s = "ABCDEF"
print(s[-3])  
print(s[-5])

# String Slicing
s = "ABCDEF"
print(s[1:4])    
print(s[:3])     
print(s[3:])    
print(s[::-1])

# Loop through string
s = "ABCDEF"
for char in s:
    print(char)
    
# Deleting a string
s = "ABC"
del s

# Common string methods
s = "GeeksForGeeks"
print(len(s))

s = "Hello World"
print(s.upper())
print(s.lower())

s = "   ABC   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))

# Concatenating and Repeating string
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

s = "Hello "
print(s * 3)

# Formatting String
name = "Jake"
age = 22
print(f"Name: {name}, Age: {age}")