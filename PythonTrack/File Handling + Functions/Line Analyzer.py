file_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/notes.txt"

#Total number of lines
with open(file_path, "r") as notes_file :
    notes_data = notes_file.readlines()
    number_ofLines = len(notes_data)
    print("Number of lines:", number_ofLines)

#Total number of words
words = []
with open(file_path, "r") as notes_file :
    notes_data = notes_file.read()
words =[word in words for word in notes_data.split()]
print("Number of words: ",len(words) +1)

#Total number of characters
with open(file_path, "r") as notes_file :
    notes_data = notes_file.read()
print("Total number of characters",len(notes_data))
