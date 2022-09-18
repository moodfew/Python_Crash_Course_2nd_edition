class Cat:
    def __init__(self, name, age) -> None:
        """Initialize name and age attributes"""
        self.name = name.title()
        self.age = age

    def sit(self):
        """Stimulate a cat sitting"""
        print(f"\n{self.name} has sat down.")

    def meow(self):
        """Stimulating a cat meowing"""
        print(f"\n{self.name} is mewoing.")

my_cat = Cat('luna', '3')

print(f"My cat's name is {my_cat.name}")
print(f"{my_cat.name} is {my_cat.age} years old.")

my_cat.sit()
my_cat.meow()
