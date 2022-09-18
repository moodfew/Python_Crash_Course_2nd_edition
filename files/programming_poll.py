file_name = 'programming_answers.txt'

prompt = "Enter 'quit' to quit\n"
prompt += "Why do you like programming? "

while True:
    response = input(prompt)

    if response == 'quit':
        break
    else:
        with open(file_name, 'a') as f:
            f.write(f"{response}\n")

