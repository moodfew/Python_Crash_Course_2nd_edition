laptops = ['Hp', 'Lenovo', 'Apple', 'Dell', 'Razor']

print(laptops[2])

laptops[4] = 'Sony'
laptops.append('Samsung')

print(laptops)

laptops.insert(3, 'idk')
del laptops[3]

print(laptops)

too_expensive = laptops.pop(3)
print(f"{too_expensive} laptops are too expensive to me for now")

laptops.remove('Hp')

print(sorted(laptops))

laptops.sort()
print(laptops)

laptops.sort(reverse=True)
print(laptops)

laptops.reverse()
print(laptops)

print(len(laptops))
