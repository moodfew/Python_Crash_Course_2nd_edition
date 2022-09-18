class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.type = cuisine_type.title()

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name.title()}")
        print(f"The cuisine type is {self.type.title()}")

    def open_restaurant(self):
        print(f"{self.name.title()} is open.\n")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='Ice Cream'):
        super().__init__(name, cuisine_type)

        # Attributes
        self.flavors = []

    def list_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"\t-{flavor}")

denis_shop = IceCreamStand('Denis Shop')
denis_shop.flavors = ['vanilla', 'chocolate', 'mint']

denis_shop.describe_restaurant()
denis_shop.list_flavors()

