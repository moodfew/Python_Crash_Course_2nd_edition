favorite_numbers = {
    'denis': [9, 5, 3],
    'jonis': [2, 27, 13],
    'toni': [11, 4, 6],
    'nora': [12, 32, 15],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"-{number}")
