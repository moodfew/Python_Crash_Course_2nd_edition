def make_sandwiches(*toppings):
    print("Adding to your sandwich:")
    for topping in toppings:
        print(f"-{topping}")

make_sandwiches('salami', 'hot-sauce', 'eggs')
