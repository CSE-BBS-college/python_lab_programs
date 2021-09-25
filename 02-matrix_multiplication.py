# To write a program perform matrix multiplication

# variables [both matrix of 3*3]
matrix_1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]
matrix_2 = [[9,8,7],
            [6,5,4],
            [3,2,1]]
result_of_multiplication=[[0,0,0],
                          [0,0,0],
                          [0,0,0]]

# performing multiplication
for x in range(len(matrix_1)):
    for y in range(len(matrix_2)):
        result_of_multiplication[x][y] += matrix_1[x][y] * matrix_2[x][y] 

# printing the result of multiplication

for result in result_of_multiplication:
    print(result)

