my_file = "learning_python.txt"

my_string = ""

with open(my_file) as fileObject:
    lines = fileObject.read()

for line_of_text in lines:
    my_string += line_of_text
    my_string = my_string.replace("Python", "C")

print(my_string)