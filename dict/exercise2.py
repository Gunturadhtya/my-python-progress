# open mbox-short; count the day of email message was commit; and add that day on dictionary

fname = open('mbox-short.txt')

day = dict()
count = 0
for line in fname :
    line = line.split()
    if len(line) == 0 or line[0] != "From" : continue
    lin2 = line[2]
    day[lin2] = day.get(lin2,0) + 1


print(day)