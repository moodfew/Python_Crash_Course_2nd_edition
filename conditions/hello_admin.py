users = ['denis', 'jonis', 'toni', 'admin', 'aleks', 'esned']

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user.title()} would you like to see the status report?")
        else:
            print(f"Hello {user.title()}, nice to see you here.")

else:
    print("We need more users.")
