file_path = "/home/aniket-deshkar/PycharmProjects/Path2AI/PythonTrack/File Handling + Functions/"

message1 = "INFO: Application started."
message2= "DEBUG: Initializing components."
message3= "INFO: User logged in."
message4= "WARN: Low disk space."
message5= "ERROR: Failed to load configuration log_file."
message6= "INFO: Request processed successfully."
message7= "DEBUG: Connection established."
message8= "INFO: Application stopped."

print("Writing into log_file")
with open(file_path+"log_writer_file.txt", "w") as log_file :
    log_file.write(message1 +"\n" )
    log_file.write(message2+"\n")
    log_file.write(message3+"\n")
    log_file.write(message4+"\n")
    log_file.write(message5+"\n")

print("Data in log file: \n")
with open(file_path+"log_writer_file.txt", "r") as log_file :
    log_data = log_file.read()
    print(log_data)

print("Appending into log_file")
with open(file_path+"log_writer_file.txt", "a") as log_file :
    log_file.write(message6+"\n")
    log_file.write(message7+"\n")
    log_file.write(message8+"\n")

print("Reading the updated log_file: \n")
with open(file_path+"log_writer_file.txt", "r") as log_file :
    log_data = log_file.read()
    print(log_data)
