
import os

for root, dirs, files in os.walk('/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/Traffic_Controller/Schema_process_NP'):
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension == '.txt':
            f = open(file, 'r')
            lines = f.readlines()
            mystr = ''.join([line.strip() for line in lines])
            #file_object = open('Solution-Schemas-202-302.txt', 'a')
            #file_object.write(mystr)
            #file_object.close()
            print(mystr)
            f.close()
            # a = file
            # print(a)

# for file in a:
