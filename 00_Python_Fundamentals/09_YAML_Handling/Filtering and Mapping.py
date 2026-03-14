marks = [45,78,88,32,90,67]

greater_than_sixty = [x for x in marks if x > 60]
print("Marks greate than 60: ", greater_than_sixty)
squared_marks = [x**2 for x in marks]
print("Squared Marks: ",squared_marks)
result_check = ['pass' if x>60 else 'fail' for x in marks ]
print("Result Check: ", result_check)
