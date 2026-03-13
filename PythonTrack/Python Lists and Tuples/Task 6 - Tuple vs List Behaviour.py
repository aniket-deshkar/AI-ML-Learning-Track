#Task 6 - Tuple vs List Behaviour
list6 = [1,2,3,4,5]
tuple6 = (1,2,3,4,5)
print("List:",list6)
print("Tuple:",tuple6)
list6[2] = 6
print("List after append: ",list6)
tuple6[2] = 6
print("Tuple after append",tuple6)
#Since list is mutable, we can change elements, whereas if the same operation of reassigning an index for a tuple throws TypeError as elow as it doesn't support item assignment.
# TypeError                                 Traceback (most recent call last)
# Cell In[50], line 8
#       6 list6[2] = 6
#       7 print("List after append: ",list6)
# ----> 8 tuple6[2] = 6
#
# TypeError: 'tuple' object does not support item assignment

