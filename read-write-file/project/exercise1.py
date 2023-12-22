# Module to delete data file
import os

# Loop function for input
def write_data_loop(filename):
    try:
        while True:
            data = input("> ")

            # If input is done the program stop
            if data == "done" :
                break
            
            # statement so that any input other than integer cant get trough to data
            int(data)

            # statement to write input into data as a string
            with open(filename, 'a') as f:
                str(data)
                f.write(data + ' ')
                
            print(data)
        # function to calculate all input on data file
        calculate_data(filename)

    # if input is other than integer, except will run write_data_loop function
    except:
        print("Invalid input")
        write_data_loop(filename)

# function to calculate all input on data file
def calculate_data(filename):

    # this statement will make input on data file become list
    with open(filename, 'r') as w:
        data = w.readline()
        number=data.split()
        
    # this statement will convert list to integer
    convert=list(map(int, number))
    
    # calculate sum, how many input, and average on the list
    total=sum(convert)
    count=len(convert)
    avg=float(total/count)

    print(total, ' ', count, ' ', avg)
        
# program executed from here
filename = "data.txt"
write_data_loop(filename)
# remove data file so that i can use it again
os.remove(filename)

