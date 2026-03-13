x =10
def modify():
    global x
    x = 20
    print(x)
modify()
print(x)

#Using 'global' keyword and assigning in local module, it overrides the predefined value
