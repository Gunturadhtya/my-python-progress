# open file romeo.txt
fname = open("romeo.txt")

word = []

# for loop; append line on romeo to list word; if the line already on list it'll not append it;
# and sort the line in alphabetical order
for lines in fname:
    lines = lines.split()
   
    for line in lines:
        if line not in word:
            word.append(line)
        word.sort()

# print word
print(word)
