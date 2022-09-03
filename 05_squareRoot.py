# Program to find square root of a number using Newton's method
# You can visit below link to learn about Newton's Method
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,to%20be%20N%20or%201.

def squareRoot(n, l):
    # Assuming the sqrt of n as n only
    x = n
    # To count the number of iterations
    # count = 0
    while(1):
        # count+=1
        # Calculate more closed x
        root = 0.5 * (x+(n/x))
        # Check for clooseness
        if(abs(root - x)<l):
            break
        # Update root
        x = root
    return root

n = 216
l = 0.00001
print(squareRoot(n, l))
