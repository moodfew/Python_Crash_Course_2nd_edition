def build_profile(first, last, **user_info):
    user_info['first'] = first.title()
    user_info['last'] = last.title()
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location = 'princeton',
                             field = 'physics')

print(user_profile)
