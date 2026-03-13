#Task 5 - Duplicate Finder
list5 = [1,2,3,4,5,2,4,6,7,1]
duplicate_list = []
print("Original List: ",list5)
for i in list5:
    if i not in duplicate_list and list5.count(i)>1:
        duplicate_list.append(i)
print("List with duplicates",duplicate_list)
