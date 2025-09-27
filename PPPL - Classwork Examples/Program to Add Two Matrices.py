#Program to Add Two Matrices

import numpy as np

matrix_size = int(input("Enter matrix size: "))

matrix1 = np.zeros((matrix_size, matrix_size), dtype=int)
matrix2 = np.zeros((matrix_size, matrix_size), dtype=int)
result = np.zeros((matrix_size, matrix_size), dtype=int)


print("Enter elements for matrix one")
for row in range(matrix_size):
    for col in range(matrix_size):
        print("Enter number for row",row,"column",col,":-",end ="")
        matrix1[row][col] = int(input())
        
print("Enter elements for matrix two")
for row in range(matrix_size):
    for col in range(matrix_size):
        print("Enter number for row",row,"column",col,":-",end ="")
        matrix2[row][col] = int(input())
        
for row in range(matrix_size):
    for col in range(matrix_size):
        result[row][col] = matrix1[row][col] + matrix2[row][col]

print("Addition of two matrix is:- ")
print(result)

