favorite_places = {
    'denis': ['america', 'france', 'greece'],
    'jonis': ['germany', 'finland', 'iceland'],
    'toni': ['greece', 'japan', 'luxemburg'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"-{place.title()}")
