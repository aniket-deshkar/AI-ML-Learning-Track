def get_element(lst,idx):
    output = 0
    try:
        output = lst[idx]
    except IndexError as error:
        print(error,"- Insert index within list length.")
    return output

value_1 = get_element([1,2,3,4,5,6],3)
print("Value 1: ",value_1)
value_2 = get_element([1,2,3,4,5],6)
print("Value 2: ", value_2)