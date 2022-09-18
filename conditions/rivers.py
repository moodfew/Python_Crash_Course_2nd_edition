rivers = {
    'egypt': 'nile',
    'albania': 'drini',
    'america': 'amazon',
}

for country,  river in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

print("The rivers:")
for river in rivers.values():
    print(f"-{river.title()}")

print("The countries:")
for country in rivers.keys():
    print(f"-{country.title()}")
