current_users = ['denis', 'jonis', 'toni', 'leonora', 'salihe']
new_users = ['zyber', 'aleks', 'toni', 'esned', 'jonis']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} you need to enter another username.")
    else:
        print(f"{new_user} is available")
