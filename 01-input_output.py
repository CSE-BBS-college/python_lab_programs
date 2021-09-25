# To write a program that takes in commond line arguments as input and print that number of arguments

# variables
no_of_arguments=1 #It is set to one by default because we expect user to enter at least one argument/word/cherecter

# Taking the input from user
value=input("Please enter your command \n")
# print(value)

# looking for arguments/words in the entered value
for x in value:
    if x == " ":
        no_of_arguments+=1

# printing the number of arguments
print(no_of_arguments)