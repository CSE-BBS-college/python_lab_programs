# Progarm to find most frequent word in a text file 
# file name should added and opened with reading mode
file = open("file_name.txt","r")
frequent_word = " "
frequency = 0
words = []
# Traversing file line by line
for line in file:
    '''splits each line into words and removing space
       and punctuations from the input'''
    line_word = line.lower().replace(',', '').replace('.', '').split(" ");

    # Adding them to list words
    for w in line_word:
        words.append(w)

for i in range(0, len(words)):
    # Declaring count
    count = 1

    # count each word in the file
    for j in range(i+1, len(words)):
        if(words[i] == words[j]):
            count = count+1
            
    # If the count value is more then highest frequency then
    if(count>frequency):
        frequency = count
        frequent_word = words[i]

print("Most repeated word: " + frequent_word)
print("Frequency: "+ str(frequency))
file.close()
