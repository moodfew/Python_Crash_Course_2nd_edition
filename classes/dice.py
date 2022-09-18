from random import randint

class Die:
    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

d6 = Die()
results = []

for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)

print("10 rolls of a dice wiht 6 sides:")
print(results)
