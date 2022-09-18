file_name = 'guest.txt'

guest = input("What is your name: ")
with open(file_name, 'w') as file_object:
    file_object.write(guest)

