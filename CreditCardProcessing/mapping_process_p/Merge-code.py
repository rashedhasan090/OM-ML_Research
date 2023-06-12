import os

directory = os.getcwd()

for root, dirs, files in os.walk(directory):
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension == '.txt':
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                lines = f.readlines()
                mystr = ''.join([line.strip() for line in lines])
                # Perform your desired operations on mystr here
                print(mystr)
