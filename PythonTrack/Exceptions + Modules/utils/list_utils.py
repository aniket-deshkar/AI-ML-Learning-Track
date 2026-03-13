def unique_elements(lst):
    unique_lst = []
    for items in lst:
        if items not in unique_lst:
            unique_lst.append(items)
    print("Unique List Elements: ",unique_lst)