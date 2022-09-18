class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.type = cuisine_type.title()

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name.title()}")
        print(f"The cuisine type is {self.type.title()}")

    def open_restaurant(self):
        print(f"{self.name.title()} is open.\n")



