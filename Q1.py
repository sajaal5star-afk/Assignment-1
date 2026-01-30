# write a program take 1d integer array nd convert that array into numpy or panda.
import numpy as np
import pandas as pd

n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

np_array = np.array(arr)
pd_series = pd.Series(arr)

print("Original Python list:", arr)
print("Converted NumPy array:", np_array)
print("Converted pandas array: ", pd_series)
