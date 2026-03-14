class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__ (self,other):
        x = self.x + other.x
        y = self.y + other.y
        sum = x + y
        return sum
    
value_1 = Vector(10,20)
print("Value 1: ", value_1)
print(type(value_1))
value_2 = Vector(20,30)
print("Value 2: ", value_2)

output = value_1 + value_2
print("Output: ", output)


