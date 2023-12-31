# this function print all text in uppercase
def uppercase():
    fname = input("Enter File Name : ")

    fopen = open(fname, 'r')
    for f in fopen:
        data = f.upper()
        print(data)

uppercase()