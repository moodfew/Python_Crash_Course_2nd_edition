file_name = 'py_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

py_string = ''
for line in lines:
    py_string += line.strip()

birthday = input("Enter you birthday in mmddyy: ")

if birthday in py_string:
    print("Your birthday is in the first million digits of py.")
else:
    print("Your birthday does not appear in the first million digit of py.")
