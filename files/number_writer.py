import json

numbers = [2, 5, 76, 98, 6, 9, 12, 27]

filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

