prompt = "Enter the topping you want in your pizza: "

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} right now.")
