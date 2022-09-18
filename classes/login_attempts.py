class User:
    def __init__(self, first_name, last_name, username, email, location, phone_number):
        """Simple information about a user"""

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location
        self.phone_number = int(phone_number)
        self.login_attempts = 0

    def describe_user(self):
        """Printing user info"""
        print(f"\nFirst name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print(f"Phone number: {self.phone_number}")

    def greet_user(self):
        """Greeting the user"""
        print(f"\nWelcome back {self.username}")

    def increment_login_attempts(self):
        """Incrementing login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resseting the login attempts"""
        self.login_attempts = 0

denis = User('Denis', 'Rrapaj', 'moodfew', 'rrapajdenis2006@gmail.com', 'Albania', '0693378508')
denis.describe_user()
denis.greet_user()

print("\nMaking 3 login attempts")
denis.increment_login_attempts()
denis.increment_login_attempts()
denis.increment_login_attempts()
print(f"Login attempts: {denis.login_attempts}")

print("\nReseting the attempts")
denis.reset_login_attempts()
print(f"Login attempts: {denis.login_attempts}")


