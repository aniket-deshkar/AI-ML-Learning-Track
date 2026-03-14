def read_file(filename):
    try:
        with open(filename,"r") as file:
            content = file.readlines()
            if not content:
                return "File is empty"
            return [lines.split("\n") for lines in content]
    except FileNotFoundError as error:
        print(error)
    except Exception as error:
        print("unexpected error",error)


print("File 1: ")
read_file("file1.txt")
print("File 2: ")
file_2 = read_file("/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/Exceptions + Modules/notes.txt")
print(file_2)