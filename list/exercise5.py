num_list = []

while True:
    get_input=input("Enter a Number : ")

    if get_input == "done":
        break

    get_input = float(get_input)

    num_list.append(get_input)

print(f"Maximum : {max(num_list)}\nMinimum : {min(num_list)}\n")

