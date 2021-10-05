def find(list, x):
    for key, element in enumerate(list):
        if element == x:
            return key
    return -1

my_list = ['a', 'b', 'c', 'd', 'c']
print(find(my_list, 'c'))