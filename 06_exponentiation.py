# Program to compute exponentiation (power of a number)

base = 3
exponent = 4
result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))
