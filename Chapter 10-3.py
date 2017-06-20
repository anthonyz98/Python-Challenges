file_name = "guest.txt"

name = input("What is your name? ")

with open(file_name, "a") as object_file:
    object_file.write(name)