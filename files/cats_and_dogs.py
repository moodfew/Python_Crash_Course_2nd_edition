filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"Reading file {filename}")

    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"Sorry the file {filename} does not exist.")

