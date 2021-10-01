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


# Write a python program find the maximum of a list of numbers.

def MaxNum(lst):
    var = lst[0]
    for a in lst:
        if a > var:
            var = a
    print(var)


MaxNum([34, 65, 76, 34, 23])



# Write a python program for linear search.

def Linear_search(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            print(f'Element {num} is present at index {i}')
    return -1


Linear_search([1, 2, 3, 4, 5], 10)



# Write a program to find first n prime numbers.

def prime():
    lower = int(input("Enter number to start checking the prime: "))
    upper = int(input("Enter number to end checking the prime: "))

    for num in range(lower, upper + 1):

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


prime()


# Write a python program for selection sort.

A = [64, 25, 12, 22, 11]


for i in range(len(A)):

    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]


print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i]),


# Write a python program for insertion sort.

def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])


