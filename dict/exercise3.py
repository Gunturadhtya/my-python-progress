# open mbox-short.txt; read through a mail log; count how many message come from an account; and add it on dictionary

fname = open('mbox-short.txt') # open mbox-short.txt

mailbox = dict() # make a dictionary data type

for line in fname : # make a for loop
    line = line.split() # split line on mbox-short
    if len(line) == 0 or line[0] != 'From': continue # if length of line is 0 or first word is not From continue
    mailine = line[1] # variable mailine equal line second word
    mailbox[line[1]] = mailbox.get(mailine, 0) + 1 # add line second word as key and get mailine ( line second word is in dictionary ) value + 1; else return 0
print(mailbox)

