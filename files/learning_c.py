file_name = 'learning_python.txt'

with open(file_name) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('python', 'C'))

