import numpy as np

a = [1, "Hello", [3.14, "world"]]
a.append(2)
print(a)

a = np.array([1, 2, 3, 4])

# Element wise operations
print(a * 2)

# Multi-dimensional array
res = np.array([[1,2], [3,4]])
print(res * 2)