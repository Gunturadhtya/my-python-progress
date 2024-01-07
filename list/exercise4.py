fhand = open('mbox-short.txt')

count = 0
for lines in fhand:
    word = lines.split()
    if len(word) == 0 or word[0] != "From" : continue
    count = count + 1
    print(word[1])
print(f"There were {count} lines in file with From as the first word")