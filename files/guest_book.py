file_name = 'guest.txt'

while True:
    guest = input("What is your name? ")

    if guest == 'quit':
        break
    else:
        print(f"Hello {guest.title()}")

        with open(file_name, 'a') as f:
            f.write(f"{guest}\n")
