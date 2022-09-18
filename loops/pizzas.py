pizzas = ['pepperoni', 'margarita', 'spicy']
friend_pizzas = pizzas[:]

pizzas.append('eggs')
friend_pizzas.append('mushrooms')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(f"-{pizza}")

print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"-{pizza}")
