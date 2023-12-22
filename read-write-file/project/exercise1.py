import os

def write_data_loop(filename):
    try:
        while True:
            data = input("> ")

            if data == "done" :
                with open(filename, 'r') as w:
                    line=w.read()
                    print(line)
                break

            int(data)

            with open(filename, 'a') as f:
                str(data)
                f.write(data + ' ')
                
            print(data)
    except:
        print("bad input")
        write_data_loop(filename)

        
filename = "data.txt"
write_data_loop(filename)
os.remove(filename)