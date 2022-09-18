file_name = 'alice.txt'

try:
    with open(file_name) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry the file {file_name} does not exist")

else:
    # Count the words
    words = contents.split()
    num_words = len(words)

    print(f"The file {file_name} has {num_words} words in it.")
