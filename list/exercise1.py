
# This Function chop the first and last member of list and return None
def chop(t):
    del t[0]
    del t[-1]
    return None

lis = [1,2,3,4,5,6,7,8,9]
print(lis, '\n')

chlis = chop(lis)

print(chlis, '\n')
print(lis, '\n')

# This function return all member of list but first and last member
def middle(t):
    return t[0:-1]

midlis = middle(lis)

print(midlis)