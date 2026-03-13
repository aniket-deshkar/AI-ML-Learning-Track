# file1 = open("/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/sample_data.txt")
# data = file1.readline()
# print(data)
# var2 = file1.readline()
# print(var2)
# data3 = file1.readlines()
# print(data3)
# file1.close()
#
data2 = "Hello World! \n"
file2 = open("/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/write_data.txt", 'w')
file2.write(data2)
file2.close()

file3 = open("/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/write_data.txt")
data3 = file3.readline()
print(data3)
file3.close()

data4 = "new Hello World Order! \n"
file4 = open("/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/write_data.txt", 'a')
file4.write(data4)
file4.close()

file7 = open("/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/write_data.txt")
data7 = file7.readline()
print(data7)
file7.close()





