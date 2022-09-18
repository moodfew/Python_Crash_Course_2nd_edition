class User:
    def __init__(self, first_name, last_name, username, email, location, phone_number):
        """Simple information about a user"""

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location
        self.phone_number = int(phone_number)

    def describe_user(self):
        print(f"\nFirst name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print(f"Phone number: {self.phone_number}")

    def greet_user(self):
        print(f"\nWelcome back {self.username}")

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location, phone_number):
        super().__init__(first_name, last_name, username, email, location, phone_number)

        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            print("Privileges:")
            for privilege in self.privileges:
                print(f"\t-{privilege}")
        else:
            print("This user has no privileges.")
