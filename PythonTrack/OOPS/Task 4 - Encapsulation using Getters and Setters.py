class Student:
    def __init__(self,marks = 0):
        self.__marks = marks

    @property
    def marks(self):
        print("Getting marks")
        return self.__marks

    @marks.setter #property_name.setter
    def marks(self,value):
        print("Setting marks")
        if value < 0 or value > 100 :
           value = print(input("Invalid marks input, enter in range of 0 to 100: \n"))
           self.__marks = value
        else:
            self.__marks = value
        
student1 = Student()
student1.marks = int(input("Enter marks: "))





