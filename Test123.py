import numpy as np

"""
Numbers = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

Numbers2 = Numbers * 2

print(Numbers)


Numbers = np.arange(100, 50, -2)

print(Numbers)
"""

grades = np.array([[80, 90, 100], [85, 85, 90], [70, 60, 42], [100, 95, 98]])
print(grades)
"""
Column_means = grades.mean(axis=0)
print(Column_means)

Row_means = grades.mean(axis=1)
print(Row_means)

Sum = np.add(grades[1], grades[2])
print(Sum)

Some_Grades = grades[0:2]
print(Some_Grades)
"""
'''
grades2 = grades.view()

grades2[0][1] *= 3

print(grades)

grades = pd.Series([50, 60, 70], index=["Braxton", "Ryan", "John"])

print(grades["Braxton"])
print(grades.Braxton)

grades = {
    "Braxton": [1, 2, 3, 4, 5],
    "Ryan": [6, 7, 8, 9, 10],
    "John": [11, 12, 13, 14, 15],
}


grades_dataframe = pd.DataFrame(grades)
grades_dataframe.index = ["Test1", "Test2", "Test3", "Test4", "Test5"]
print(grades_dataframe)
print()
print(grades_dataframe["Braxton"])
print()
print(grades_dataframe.iloc[1])
print()
print(grades_dataframe.loc["Test2"])
'''

array123 = np.full([4,5], 13)

print(array123)

