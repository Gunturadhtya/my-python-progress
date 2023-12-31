def XDSPAM():
    fname = input("Input File Name : ") # mbox-short.txt

    # Easter EGG just for you!!!!! :>
    if fname == 'na naa bo boo':
            print("NA NAA BO BOO TO YOU - you have been punked")
            exit()

    # Secure Guard
    try : 
        fh = open(fname)
    except :
        print(f"file {fname} cannot be opened")
        exit()

    # GO TAKE THE NUMBER AFTER BLABLABLA-CONFIDENCE AND CALCULATE THE AVERAGE
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