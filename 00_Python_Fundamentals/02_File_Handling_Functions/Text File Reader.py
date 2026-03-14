import json
file_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/notes.txt"
with open(file_path, "r") as notes_file:
    notes_data = notes_file.read()
print(notes_data)


#using readline()
with open(file_path, "r") as notes_file:
    print(".readline() prints each line individually")
    for note in notes_file :
        notes_data = notes_file.readline()
        print(notes_data)

#using readlines()

with open(file_path, "r") as notes_file:
    print(".readlines() prints in single line")
    notes_data = notes_file.readlines()
    print(notes_data)






