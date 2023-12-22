import os

def write_data_loop(filename):
    try:
        while True:
            data = input("> ")

            if data == "done" :
                calculate_data()
                break

            int(data)

            with open(filename, 'a') as f:
                str(data)
                f.write(data + ' ')
                
            print(data)
    except:
        print("bad input")
        write_data_loop(filename)

def calculate_data(filename):
    with open(filename, 'r') as w:
        data = w.readlines()
        for number in data:
            count = number.split()
            print(count)

filename = "data.txt"
write_data_loop(filename)
os.remove(filename)