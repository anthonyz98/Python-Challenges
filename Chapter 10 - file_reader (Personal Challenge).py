import json

filename = "pi_digits.txt"

with open(filename) as file_object: # The "filename" is stored into object "file_object"
    for line in file_object:
        print(line.rstrip())

    print("\n")

""" How to make a list of lines from a file """
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("\n")

pi_string = ""
for line in lines:
    pi_string += line.strip() # This helped to put every digit in one line

print(pi_string)
print(len(pi_string))
print("\n")

"""Print the first 50 of 100 digits"""
file_name_2 = "pi_100_digits.txt"
pi_string_100 = ""
number_in_file = len(pi_string_100)

with open(file_name_2) as file_object:
    new_lines_file = file_object.readlines()

for another_line in new_lines_file:
    pi_string_100 += another_line.strip() # This helped to put every digit in one line

print(pi_string_100[:52] + "...")

"""Print a new line after a tenth digit"""

for character in new_lines_file:
    if new_lines_file[character] % 10 == 0:
        new_lines_file.insert(character, "\n")

experimental_length_of_file = len(new_lines_file)

json_string = json.dumps(new_lines_file)
print(json_string)