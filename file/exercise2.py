def XDSPAM():
    fname = input("Input File Name : ") # mbox-short.txt
    fh = open(fname)
    text = "X-DSPAM-Confidence:"
    som=0
    count=0
    for line in fh:
        if not line.startswith(text):
            continue
        floatline = float(line[20:])
        som += floatline
        count += 1
    print("Average spam confidence:", som/count)

XDSPAM()