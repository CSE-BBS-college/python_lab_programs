
# variables
matrix_a = [[0],[0]]
matrix_b = [[0],[0]]
result = [[0],[0]]

# choosing the opration
print("Welocome to the Py-matrix-solver!\n\n Please select the matrix opration [1-4] \n [1] - Addition \n [2] - Substraction \n [3] - Multiplication \n [4] - Division")

name_of_opration = int(input(""))

# Taking the no. of matrix
print("Please select the no. of matrix [1-2]")
no_of_matrix = int(input(""))

# Taking the number of rows and cols
if no_of_matrix == 1:
        count_of_matrix_a=input("Please select the no. of rows and cols in matrix A [x*y]").split('*')
        print(count_of_matrix_a)
        
elif no_of_matrix == 2:
        count_of_matrix_a=input("Please select the no. of rows and cols in matrix A [x*y]").split('*')
        count_of_matrix_b=input("Please select the no. of rows and cols in matrix B [x*y]").split('*')

# taking the value for matrix 
if no_of_matrix == 1:
    values_for_matrix_a=input("Please enter the values for matrix A [values will be seprated by comma ex: 19,20]").split(',')
    # print(values_for_matrix_a)
elif no_of_matrix == 2:
    values_for_matrix_a=input("Please enter the values for matrix A [values will be seprated by comma ex: 19,20]").split(',')
    values_for_matrix_b=input("Please enter the values for matrix b [values will be seprated by comma ex: 19,20]").split(',')

# creating matrix with the entered values
def createMatrix(values,count,mat_variable):
    for x in range(len(values)):
        values[x] = int(values[x])

    # for i in range(0,len(values),int(count[1])):
    #     yield values[i:int(i+int(count[1]))]


        #####################################
        #
        #ToDo
        # continue the function
        #
        #
        #####################################
    # for x in range(int(count[0])-1):
    #     for y in range(int(count[1])-1):
    #         mat_variable[x].insert(y-1,values[i])
    #         i+=1

    # if no_of_matrix == 1:
    #     createMatrix(values_for_matrix_a,count_of_matrix_a,matrix_a)
    # elif no_of_matrix == 2:
    #     createMatrix(values_for_matrix_a,count_of_matrix_a,matrix_a)
    #     createMatrix(values_for_matrix_b,count_of_matrix_b,matrix_b)

createMatrix(values_for_matrix_a,count_of_matrix_a,matrix_a)


# def tempConstructor(matrix,count):
#     for x matrix
   

# print(type(int(count_of_matrix_a[1])))
print(values_for_matrix_a)


# print(count_of_matrix_a,count_of_matrix_b)

       
# To write a program perform matrix multiplication

# variables [both matrix of 3*3]
# matrix_1 = [[1,2,3],
#             [4,5,6],
#             [7,8,9]]
# matrix_2 = [[9,8,7],
#             [6,5,4],
#             [3,2,1]]
# result_of_multiplication=[[0,0,0],
#                           [0,0,0],
#                           [0,0,0]]

# # performing multiplication
# for x in range(len(matrix_1)):
#     for y in range(len(matrix_2)):
#         result_of_multiplication[x][y] += matrix_1[x][y] * matrix_2[x][y] 

# # printing the result of multiplication

# for result in result_of_multiplication:
#     print(result)

