import scipy.linalg
import numpy as np

n = 4
#k = 27.
#p=21
#s = 0,02*k
#B= 0.02*k
matrix = np.array(
    [[8.3, 2.62, 4.1, 1.9], [3.92, 8.45, 7.78, 2.46], [3.77, 7.21, 8.04, 2.28], [2.21, 3.65, 1.69, 6.69], ])
reverse_matrix = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
#print(np.linalg.inv(matrix))
print(matrix)

for y in range(0, n, 1):
    number = matrix[y][y]
    for i in range(y, n, 1):
        reverse_matrix[y][i] = reverse_matrix[y][i] * 1/number
        matrix[y][i] = matrix[y][i] * 1 / number

    for x in range(y + 1, n, 1):
        number = matrix[x][y]
        for i in range(y, n, 1):
            reverse_matrix[x][i] = reverse_matrix[x][i] - reverse_matrix[y][i]* number
            matrix[x][i] = matrix[x][i] - matrix[y][i] * number

for x in range(0, 3, 1):
    for y in range(1 + x, 4, 1):
        number = matrix[x][y]
        for i in range(y, n, 1):
            reverse_matrix[x][i] = reverse_matrix[x][i] - reverse_matrix[y][i]*number
            matrix[x][i] = matrix[x][i] - matrix[y][i] * number

print(reverse_matrix)
print(np.dot(np.linalg.inv(matrix),matrix))