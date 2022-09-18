guests = ['Leonora', 'Kliton', 'Jonis', 'Salihe', 'Zyber', 'Esned']

# Inviting
print(f"Hello {guests[0].title()}, you are invited to a dinner.")
print(f"Hello {guests[1].title()}, you are invited to a dinner.")
print(f"Hello {guests[2].title()}, you are invited to a dinner.")
print(f"Hello {guests[3].title()}, you are invited to a dinner.")
print(f"Hello {guests[4].title()}, you are invited to a dinner.")
print(f"Hello {guests[5].title()}, you are invited to a dinner.")

print(f"{guests[5].title()} can't make it.")
removed_guest = guests.pop(5)
guests.insert(5, 'Amri')


# Inviting
print(f"Hello {guests[0].title()}, you are invited to a dinner.")
print(f"Hello {guests[1].title()}, you are invited to a dinner.")
print(f"Hello {guests[2].title()}, you are invited to a dinner.")
print(f"Hello {guests[3].title()}, you are invited to a dinner.")
print(f"Hello {guests[4].title()}, you are invited to a dinner.")
print(f"Hello {guests[5].title()}, you are invited to a dinner.")


print("I found a bigger table")
guests.insert(0, 'Aleks')
guests.insert(3, 'Diamant')
guests.append('Idk')


print(f"Hello {guests[0].title()}, you are invited to a dinner.")
print(f"Hello {guests[1].title()}, you are invited to a dinner.")
print(f"Hello {guests[2].title()}, you are invited to a dinner.")
print(f"Hello {guests[3].title()}, you are invited to a dinner.")
print(f"Hello {guests[4].title()}, you are invited to a dinner.")
print(f"Hello {guests[5].title()}, you are invited to a dinner.")
print(f"Hello {guests[6].title()}, you are invited to a dinner.")
print(f"Hello {guests[7].title()}, you are invited to a dinner.")
print(f"Hello {guests[8].title()}, you are invited to a dinner.")

print("I can only invite 2 people to the dinner.")

removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}")

print(f"{guests[0].title()} you are still invited")
print(f"{guests[1].title()} you are still invited")
del guests[0]
del guests[0]
print(guests)
