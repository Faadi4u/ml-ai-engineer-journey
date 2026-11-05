import pandas as pd

## 1. Series
scores_1 = pd.Series([1,3,65,89,34]);

print(scores_1)

## 2. Custom labled Series:

sccores_2 = pd.Series([19,39,65,89,34],
                      index= ["Ali", "Fahad", "Salman", "Usman,", "Abdullah"],
                      name = "Exam_Scores" );

print(sccores_2)
print(sccores_2["Fahad"])
print(sccores_2.index)
print(sccores_2.dtype)
print(sccores_2.ndim)
print(sccores_2.size)

#......................................................................................................................................

## DataFrame
# Create a DataFrame from a dictionary:

students = pd.DataFrame({
    "student": ["Fahad", "Abdullah", "Umar", "Sulman", "Usman", "Abbas"],
    "hours_studied": [1.5, 0, 5,8,3,6],
    "attendance": [80, 87,76,27,25,78],
    "score": [72, 95, 68, 84,98,95],
}, index= ["one", "two", "three", "four", "five","six"], )

print(students)
print("Shape", students.shape)
print("Size", students.size)
print("Dimension", students.ndim)
print("Data_Type", students.dtypes)
print("Coloumns", students.columns)

# ## Dataset Inspection
print(students.info()) #Column types, non-null counts, index, and memory information
print(students.head()) #First five rows by default
print(students.tail()) #Last five rows by default
print(students.describe())
