class Student:
    school_name = "ABC Academy"

#printing from class object
print("Directly calling from class object: ",Student.school_name)
Student.school_name ="First Update of School Name"
print("Printing First Instance of update: ", Student.school_name)

#Creating instance of class Student
new = Student()
new.school_name = "Montfort School"
print("After modifying instance : ",new.school_name)

#Updating class instance updates the original value for all instances, whereas updating the variable instance only updates for that instance