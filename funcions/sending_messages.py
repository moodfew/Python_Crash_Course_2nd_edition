def show_message(messages):
    """Printing messages"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ['hey bitch', 'cpd', 'vrk']
show_message(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("The following lists:")
print(messages)
print(sent_messages)
