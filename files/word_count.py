def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    else:
        words = contents.split()
        num_words = len(words)

        print(f"The file {filename} has {num_words} words in it.")

filename = 'alice.txt'
count_words(filename)
