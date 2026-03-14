list2 = [1,2,3,4,5]
print(list2)
list2[0] = 6
print("First element change",list2)
list2[-1]   = 7
print("Last element change",list2)
list2.clear()
#Since list is unordered and mutable, we can change the values at any given index making it dynamic.