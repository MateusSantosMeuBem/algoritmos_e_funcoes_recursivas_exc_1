def returnNumber(n):
    if str(n).replace('.', '').isdigit() and str(n).count('.') <= 1:
        n = float(n)
        if int(str(n).split('.')[1]) == 0:
            n = int(n)

        return n

    return None

# Main function
def minList(list):
    counter = 0
    for n in list:
        if returnNumber(n) != None:
            min = returnNumber(n)
            counter = 1
            break
    if counter:
        if len(list)  > 0:
            for element in list:
                new_element = returnNumber(element)
                if new_element != None and new_element < returnNumber(min):
                    min = element
        return min, type(min)

    else:
        return None

my_list = ['test', 6, '10.0.0', 1, 8, 9.5, 9, '7', '7.9']
print(minList(my_list))
