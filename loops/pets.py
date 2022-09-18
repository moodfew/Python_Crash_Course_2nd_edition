pets = {
    'maxi': {
        'animal_type': 'dog',
        'owner': 'aleks',
    },
    'luna': {
        'animal_type': 'cat',
        'owner': 'miri',
    },
    'leksi': {
        'animal_type': 'dog',
        'owner': 'denis',
    },
}

for animal, animal_info in pets.items():
    print(f"Animal name: {animal.title()}")
    animal_type = animal_info['animal_type']

    print(f"Animal type: {animal_type.title()}")
    animal_owner = animal_info['owner']

    print(f"The animal owner is: {animal_owner.title()}\n")
