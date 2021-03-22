import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# Rows - grades for each student
# Cols - grades for each test

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis=0)  # axis = 0 is by column (test)
print(g)

h = grades.mean(axis=1)  # axis = 1 is by row (student)
print(h)
