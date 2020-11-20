#lst = ["Chucks", "Ada", "Henry", "Benita"]

#def remv(param):
#   """this is a function to remove the first and last element"""
#    param.pop(0)
#    param.pop()
#    return param

#print(remv(lst))
#new_list = remv(lst)
#print(new_list)

lst = [1, 30, 3, 40, 10]

def large(param):
    param.sort()
    print(param[-1])

large(lst)

def large(param):
    """this function takes in alist and returns the largest"""
    largest = 0
    for x in param:
        if x > largest:
            largest = x
    return largest

print(large(lst))

