class Restaurant:

    def __init__(self, name, cuisine_type):
        """Information"""
        self.name = name.title()
        self.type = cuisine_type.title()
        self.number_served = 5
    def describe_restaurant(self):
        """Describing the restaurant"""

        print(f"The restaurant name is {self.name.title()}")
        print(f"The cuisine type is {self.type.title()}")

    def open_restaurant(self):
        """Restaurant state (opened/closed)"""
        print(f"{self.name.title()} is open.\n")

    def set_number_served(self, people_served):
        """Change how many people have been served"""
        self.number_served = people_served

    def increment_number_served(self, number_customers):
        """Increment the number of people that have been served"""
        self.number_served += number_customers

restaurant = Restaurant('Denis', 'sea')
print(f"The restaurant has served {restaurant.number_served} people.")

restaurant.set_number_served(23)
print(f"The restaurant has served {restaurant.number_served} people.")

restaurant.increment_number_served(105)
print(f"The restaurant has served {restaurant.number_served} people.")

