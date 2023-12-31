fname = 'mbox-short.txt'
fh = open(fname)
text = "X-DSPAM-Confidence:"
for line in fh:
    if not line.startswith(text):
        continue
    print(line[20:])
    

print("Done")
