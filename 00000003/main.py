def reverseList(list):
    reversed_list = []
    for key in range(len(list) - 1, -1, -1):
        reversed_list.append(list[key])
    return reversed_list

my_list = [1, 2, 3, 4, 5]
print(reverseList(my_list))