# write a prog. take 2d array that array convert into 1d using numpy and panda 

import pandas as pd
import numpy as np

r = int(input("Enter no. of rows: "))
c = int(input("Enter no. of columns: "))

matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split( ))))

print("Numpy Array: ")
print(np.array(matrix))

print("Panda Array: ")
print(pd.Series(matrix))