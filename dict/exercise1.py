# store all word in words.txt as key; doesnt matter what the value is; 

fname = open('words.txt')

words2dict = dict()

for line in fname:
    line = line.split()
    for word in line :
        words2dict[word] = word.upper()
print(words2dict)