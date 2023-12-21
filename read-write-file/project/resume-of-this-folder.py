import os

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write("Hello World!!\n")
        print("File " + filename + " created succesfully")
    except IOError:
        print("Error : couldnt create file" + filename)

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except IOError:
        print("Error : couldnt read file " + filename)

def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text [" + text + "] succesfully added")
    except IOError:
        print("Error : text [ \n" + text + "] couldnt be added" )
    
if __name__ == "__main__" :
    filename = "example.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This will be added as a new line\n")

    