fname = open("romeo.txt")

word = []
for lines in fname:
    lines = lines.split()
    for line in lines:
        word.append(line)
        
        repeatedWord = word.count(line)
        print(repeatedWord, ' : ' , line)
        word = sorted(word)                
print(word)
