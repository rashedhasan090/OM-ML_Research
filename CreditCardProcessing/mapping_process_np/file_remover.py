import os

directory = os.getcwd()

for item in os.listdir(directory):
    if item.endswith(".sql"):
        # or item.endswith(".xml") or item.endswith(".xml.txt") or item.endswith(".txt"):
        os.remove(os.path.join(directory, item))
